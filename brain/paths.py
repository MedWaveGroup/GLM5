"""Repository paths. BRAIN_ROOT overrides the editable-install location."""

from __future__ import annotations

import os
from pathlib import Path


def repo_root() -> Path:
    env = os.environ.get("BRAIN_ROOT")
    if env:
        return Path(env)
    return Path(__file__).resolve().parents[1]


def vault_dir() -> Path:
    return repo_root() / "vault"


def sources_dir() -> Path:
    return repo_root() / "sources"


def notes_dir() -> Path:
    return sources_dir() / "notes"


def decision_model_path() -> Path:
    return sources_dir() / "decision-model.md"


def config_path() -> Path:
    return repo_root() / "brain.toml"


def scripts_dir() -> Path:
    return repo_root() / "scripts"
