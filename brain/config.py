"""Ollama host config. Loopback only, Mac profile first, Linux profile second."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from urllib.parse import urlparse

from brain.paths import config_path


class ConfigError(ValueError):
    """Raised when a host is not loopback or the config cannot be read."""


@dataclass(frozen=True)
class Host:
    name: str
    url: str
    model: str
    hardware: str = ""


@dataclass(frozen=True)
class Settings:
    hosts: tuple[Host, ...]
    embed_model: str = "nomic-embed-text"
    health_timeout_s: float = 1.5
    generate_timeout_s: float = 90.0
    num_predict: int = 280


_DEFAULT_HOSTS = (
    Host("davide-mac", "http://127.0.0.1:11434", "qwen2.5:7b", "M3, 24 GB"),
    Host("linux-box", "http://127.0.0.1:11434", "qwen2.5:3b", "Linux box"),
)


def is_loopback(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower().strip("[]")
    return host in {"127.0.0.1", "localhost", "::1"}


def require_loopback(url: str) -> None:
    if not is_loopback(url):
        raise ConfigError(
            f"Ollama host {url} is not loopback. Tunnels and remote hosts are refused."
        )


def load_settings(path=None) -> Settings:
    path = path or config_path()
    if not path.exists():
        return Settings(hosts=_DEFAULT_HOSTS)
    with path.open("rb") as handle:
        data = tomllib.load(handle)
    hosts = []
    for row in data.get("hosts") or []:
        url = str(row["url"]).rstrip("/")
        require_loopback(url)
        hosts.append(
            Host(
                name=str(row.get("name") or url),
                url=url,
                model=str(row["model"]),
                hardware=str(row.get("hardware") or ""),
            )
        )
    if not hosts:
        hosts = list(_DEFAULT_HOSTS)
    ollama = data.get("ollama") or {}
    return Settings(
        hosts=tuple(hosts),
        embed_model=str(ollama.get("embed_model") or "nomic-embed-text"),
        health_timeout_s=float(ollama.get("health_timeout_s") or 1.5),
        generate_timeout_s=float(ollama.get("generate_timeout_s") or 90),
        num_predict=int(ollama.get("num_predict") or 280),
    )
