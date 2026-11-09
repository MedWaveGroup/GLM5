"""Loopback Ollama pool. Health-check hosts in order and fall back."""

from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Callable

from brain.config import ConfigError, Host, Settings, load_settings, require_loopback

Transport = Callable[[str, str, dict | None, float], dict]


def _urllib_transport(method: str, url: str, body: dict | None, timeout: float) -> dict:
    data = None if body is None else json.dumps(body).encode()
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method=method,
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.load(response)


def model_names(payload: dict) -> list[str]:
    names = []
    for row in payload.get("models") or []:
        name = row.get("name") or row.get("model") or ""
        if name:
            names.append(name)
    return names


def has_model(available: list[str], want: str) -> bool:
    want = want.strip()
    for name in available:
        if name == want or name.split(":")[0] == want or name.startswith(want + ":"):
            # "qwen2.5:3b" matches "qwen2.5:3b" and "qwen2.5:3b:latest"
            if name == want or name.startswith(want):
                return True
    return False


class OllamaPool:
    """Try Davide's Mac profile first, then the Linux box profile."""

    def __init__(
        self,
        settings: Settings | None = None,
        transport: Transport | None = None,
    ):
        self.settings = settings or load_settings()
        self.transport = transport or _urllib_transport
        for host in self.settings.hosts:
            require_loopback(host.url)

    def tags(self, host: Host) -> list[str]:
        require_loopback(host.url)
        payload = self.transport(
            "GET",
            host.url + "/api/tags",
            None,
            self.settings.health_timeout_s,
        )
        return model_names(payload)

    def healthy_hosts(self) -> list[tuple[Host, list[str]]]:
        found = []
        for host in self.settings.hosts:
            try:
                found.append((host, self.tags(host)))
            except ConfigError:
                raise
            except Exception:
                continue
        return found

    def pick(self, model: str | None = None) -> tuple[Host | None, str | None]:
        """Return the first healthy host whose preferred model is installed.

        A host that answers but lacks its preferred model does not win. The
        next host is tried, which is how a Linux box running only qwen2.5:3b
        is selected when both profiles share 127.0.0.1:11434.
        """
        healthy = self.healthy_hosts()
        if model:
            for host, models in healthy:
                if has_model(models, model):
                    return host, _resolve(models, model)
        for host, models in healthy:
            if has_model(models, host.model):
                return host, _resolve(models, host.model)
        if healthy:
            host, models = healthy[0]
            for cand in ("qwen2.5:3b", "qwen2.5:7b"):
                if has_model(models, cand):
                    return host, _resolve(models, cand)
            if models:
                return host, models[0]
        return None, None

    def generate(
        self,
        prompt: str,
        system: str | None = None,
        model: str | None = None,
    ) -> dict | None:
        """Generate on the first host that both has the model and answers.

        Returns None when every host fails. Callers then stay in rules-only
        mode or set the paid-model flag.
        """
        candidates = self._candidates(model)
        last_error = None
        for host, use_model in candidates:
            body = {
                "model": use_model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.1,
                    "num_predict": self.settings.num_predict,
                    "num_ctx": 4096,
                },
            }
            if system:
                body["system"] = system
            try:
                payload = self.transport(
                    "POST",
                    host.url + "/api/generate",
                    body,
                    self.settings.generate_timeout_s,
                )
            except Exception as exc:
                last_error = exc
                continue
            text = (payload.get("response") or "").strip()
            if not text:
                last_error = RuntimeError("empty response")
                continue
            return {"text": text, "model": use_model, "host": host.name, "url": host.url}
        self.last_error = last_error
        return None

    def embed(self, text: str, host: Host | None = None) -> list[float] | None:
        """Embed with nomic-embed-text when that model is on a healthy host."""
        want = self.settings.embed_model
        chosen = None
        if host is not None:
            try:
                models = self.tags(host)
            except Exception:
                models = []
            if has_model(models, want):
                chosen = host
        if chosen is None:
            for candidate, models in self.healthy_hosts():
                if has_model(models, want):
                    chosen = candidate
                    break
        if chosen is None:
            return None
        body = {"model": want, "prompt": text}
        try:
            payload = self.transport(
                "POST",
                chosen.url + "/api/embeddings",
                body,
                self.settings.generate_timeout_s,
            )
        except Exception:
            return None
        vector = payload.get("embedding")
        if not isinstance(vector, list) or not vector:
            return None
        return [float(v) for v in vector]

    def _candidates(self, model: str | None) -> list[tuple[Host, str]]:
        healthy = self.healthy_hosts()
        ranked: list[tuple[Host, str]] = []
        seen = set()

        def add(host: Host, models: list[str], want: str) -> None:
            if not has_model(models, want):
                return
            key = (host.name, want)
            if key in seen:
                return
            seen.add(key)
            ranked.append((host, _resolve(models, want)))

        for host, models in healthy:
            if model:
                add(host, models, model)
            add(host, models, host.model)
        for host, models in healthy:
            for cand in ("qwen2.5:3b", "qwen2.5:7b"):
                add(host, models, cand)
        return ranked


def _resolve(models: list[str], want: str) -> str:
    for name in models:
        if name == want or name.startswith(want):
            return name
    return want
