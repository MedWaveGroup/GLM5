"""Minimal loopback-only Ollama client for MedWave helper scripts.

Rules: loopback only (127.0.0.1 / localhost / ::1), no tunnels, no remote hosts.
No secrets are read or logged. If Ollama is down, callers get None and must
fall back to deterministic logic or flag `escalate_paid`.
"""
from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request

DEFAULT_URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434")
PREFERRED_MODELS = ("qwen2.5:7b", "qwen2.5:3b")  # Mac first, then box
LOOPBACK = {"127.0.0.1", "localhost", "::1"}
SAVINGS_LOG = os.environ.get(
    "GLM5_HELPER_SAVINGS", os.path.join(os.path.dirname(__file__), "savings_helpers.jsonl")
)


def _check_loopback(url: str) -> str:
    host = urllib.parse.urlparse(url).hostname or ""
    if host not in LOOPBACK:
        raise ValueError(f"Refusing non-loopback Ollama host: {host!r}")
    return url.rstrip("/")


def models(url: str = DEFAULT_URL, timeout: float = 2.0) -> list[str]:
    url = _check_loopback(url)
    try:
        with urllib.request.urlopen(f"{url}/api/tags", timeout=timeout) as r:
            return [m["name"] for m in json.load(r).get("models", [])]
    except Exception:
        return []


def pick_model(url: str = DEFAULT_URL) -> str | None:
    have = models(url)
    for m in PREFERRED_MODELS:
        if m in have:
            return m
    return have[0] if have else None


def _log(step: str, chars_in: int, chars_out: int, model: str | None, secs: float) -> None:
    try:
        with open(SAVINGS_LOG, "a") as f:
            f.write(json.dumps({
                "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "step": step, "local": True,
                "model": model, "chars_in": chars_in, "chars_out": chars_out,
                "est_paid_tokens_avoided": (chars_in + chars_out) // 4, "secs": round(secs, 2),
            }) + "\n")
    except OSError:
        pass


def generate(prompt: str, *, system: str = "", step: str = "generate", json_mode: bool = False,
             num_predict: int = 400, temperature: float = 0.2, url: str = DEFAULT_URL,
             timeout: float = 180.0) -> str | None:
    """Return the model's text, or None when Ollama is unavailable."""
    url = _check_loopback(url)
    model = pick_model(url)
    if not model:
        return None
    body = {"model": model, "prompt": prompt, "system": system, "stream": False,
            "options": {"temperature": temperature, "num_predict": num_predict}}
    if json_mode:
        body["format"] = "json"
    t0 = time.time()
    try:
        req = urllib.request.Request(f"{url}/api/generate", data=json.dumps(body).encode(),
                                     headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            out = json.load(r).get("response", "").strip()
    except Exception:
        return None
    _log(step, len(prompt) + len(system), len(out), model, time.time() - t0)
    return out
