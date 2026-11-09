"""Rebuild the vault. Legacy export scripts run only when a raw dump is present."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from brain.paths import decision_model_path, notes_dir, scripts_dir, vault_dir
from brain.vaultbuild import compile_vault


def ingest(
    raw: Path | None = None,
    notes: Path | None = None,
    decision_model: Path | None = None,
    out: Path | None = None,
    reindex_workspace: bool = False,
) -> dict:
    """Compile the Obsidian vault.

    When `raw` contains `memory/*.txt`, the shipped build scripts run first
    (they are the original export builders, with BRAIN_EXPORT pointed at that
    tree). They call Ollama and only make sense on a machine that still has
    the dumps. Otherwise the vault is compiled from `sources/notes`.
    """
    out = Path(out or vault_dir())
    notes = Path(notes) if notes else None
    legacy = None
    if raw is not None:
        raw = Path(raw)
        export_root = raw.parent if raw.name == "raw" else raw
        memory = export_root / "raw" / "memory"
        if not memory.exists():
            memory = raw / "memory" if (raw / "memory").exists() else None
            if memory is not None:
                export_root = raw
        if memory is not None and any(memory.glob("*.txt")):
            legacy = _run_legacy(export_root, reindex_workspace)
            produced = export_root / "notes"
            if notes is None and produced.exists():
                notes = produced
            produced_model = export_root / "decision-model.md"
            if decision_model is None and produced_model.exists():
                decision_model = produced_model
    if notes is None:
        notes = notes_dir()
    if decision_model is None:
        decision_model = decision_model_path()
    if not notes.exists():
        raise FileNotFoundError(f"No notes directory at {notes}")
    stats = compile_vault(notes, Path(decision_model), out)
    stats["legacy"] = legacy
    stats["notes_dir"] = str(notes)
    stats["out"] = str(out)
    return stats


def _run_legacy(export_root: Path, reindex_workspace: bool) -> list[dict]:
    env = os.environ.copy()
    env["BRAIN_EXPORT"] = str(export_root)
    env.setdefault("OLLAMA_MODEL", "qwen2.5:3b")
    names = ["build_brain.py", "build_decision_model.py"]
    if reindex_workspace:
        names.append("index_workspace.py")
    logs = []
    for name in names:
        script = scripts_dir() / name
        proc = subprocess.run(
            [sys.executable, str(script)],
            env=env,
            capture_output=True,
            text=True,
        )
        logs.append(
            {
                "script": name,
                "returncode": proc.returncode,
                "stderr_tail": (proc.stderr or "")[-400:],
            }
        )
    return logs
