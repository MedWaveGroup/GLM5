---
name: brain-refresh
description: Use when the Obsidian vault should be rebuilt from sources/notes, or from a raw bot export, without sending the notes to a paid model.
---

# Brain refresh

## Rule

Local first, tokens last.

`brain ingest` recompiles `vault/` on this machine. It does not call a paid model. The legacy builders in `scripts/` run only when you pass a raw export that still has `memory/*.txt`, and those builders call loopback Ollama, not a cloud model. Headroom's `compress()` is used inside those builders when `headroom-ai` is installed, and skipped when it is not.

Do not put tunnels in `brain.toml`. Hosts stay on `127.0.0.1`.

## Commands

```bash
brain ingest
brain ingest --json
brain ingest --raw /path/to/brain-export/raw
brain ingest --reindex-workspace
```

The default reads `sources/notes` and `sources/decision-model.md` and writes `vault/`, including `Start here.md` and `.obsidian/`. `--reindex-workspace` also runs `scripts/index_workspace.py`, which walks the working tree with the local model. Leave it off unless that tree is the MedWave workspace.
