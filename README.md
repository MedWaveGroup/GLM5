# MedWave manager brain

This repo is the memory Master Control answers from. It is an Obsidian vault of the 9 Nov 2026 bot-fleet export, plus a small Python CLI that spends local compute before it spends paid tokens.

Davide Duranti approved the one-time export. Emails, phone numbers, and secrets are redacted. Slack user IDs and HighLevel contact or opportunity IDs are kept.

## Layout

```
vault/          Obsidian vault. Start at vault/Start here.md
  .obsidian/    minimal config (no community plugins)
  standing-rules/   one short note per standing rule, plus the dated fact log
  team/             one note per person, plus the dated fact log
  bots/             one note per agent
brain/          Python package. Command: brain
skills/         SKILL.md files for the six commands
sources/        redacted notes, decision-model.md, manifest.json
scripts/        the original export builders (build_brain.py and the two siblings)
tools/ollama_helpers/  loopback-only Ollama helpers (no sends, no HighLevel calls)
docs/           operating knowledge base, Ollama-first process flow, gap analysis
CHANGELOG.md    dated repo changes
brain.toml      Ollama hosts, loopback only
tests/          pytest. Ollama is mocked
```

## Operating docs (12 Nov 2026)

The day-to-day operating pack lives in `docs/`. Start here:

- [Truncated knowledge base](docs/KNOWLEDGE_BASE_TRUNCATED.md) and the printable [PDF](docs/MedWave_Knowledge_Base_2026-11-12.pdf)
- [Ollama-first process flow](docs/PROCESS_FLOW.md) (diagram: [flow.png](docs/flow.png), mermaid source: [flow.mmd](docs/flow.mmd))
- [Ollama gap analysis](docs/OLLAMA_GAP_ANALYSIS.md) — what already runs locally, and the remaining gaps
- Raw Ollama drafts used to seed the knowledge base: [docs/ollama_drafts/](docs/ollama_drafts/)
- Helper scripts: [tools/ollama_helpers/](tools/ollama_helpers/)

Every task still starts with a deterministic rule or vault lookup, then local Ollama on `127.0.0.1:11434` (no tunnels). A paid model is used only when Ollama cannot do the task. See the process flow for the 13 stages, the escalation trigger, and the send gates (including the CPD no-pricing hold, monthly-finance amounts only, the 50-email daily cap, and the 24-hour skip for blasts and reactivation). The one-hour re-touch for brand-new leads stays.

See [CHANGELOG.md](CHANGELOG.md) for what landed on 12 Nov.

## Token-saving design

Routing order, every time (the full 13-stage flow is in [docs/PROCESS_FLOW.md](docs/PROCESS_FLOW.md)):

1. **A deterministic rule or a lookup.** `decide`, `triage-lead`, `assign`, and `report` answer from the standing rules with no model call when the situation matches. `ask` retrieves with BM25 (keyword search) over the vault. There are no paid embeddings.
2. **A local Ollama model.** Hosts in `brain.toml`, first match wins. Davide's Mac is `http://127.0.0.1:11434` with `qwen2.5:7b` (M3, 24 GB). The Linux box is the same loopback address with `qwen2.5:3b`. The pool health-checks `/api/tags` and falls through when a host is down or its preferred model is not installed. If `nomic-embed-text` is installed, `ask` reranks the BM25 shortlist with it. If it is not, BM25 stands.
3. **The paid-model flag.** `escalate_paid: yes` plus a reason. A human flag means Davide (Red items, spend above R5,000, external sends, open gaps), not a larger cloud model.

Before any local generation, the fact payload goes through Headroom's `compress()` when `headroom-ai` is installed. If the import fails, the CLI sends the unshrunk text and continues. No Headroom proxy is started and nothing is sent off the machine.

Loopback only. A host that is not `127.0.0.1`, `localhost`, or `::1` is refused. Do not add a tunnel.

## Setup on Davide's Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pip install headroom-ai
ollama pull qwen2.5:7b
ollama pull nomic-embed-text   # optional reranker
brain ingest
brain decide "unowned lead"
```

Ollama listens on `http://127.0.0.1:11434`. The first profile in `brain.toml` selects `qwen2.5:7b` when that model is present.

## Setup on the Linux box

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pip install headroom-ai
ollama pull qwen2.5:3b
ollama pull nomic-embed-text   # optional
brain ingest
pytest
```

The same `brain.toml` is used. The Mac profile does not match, because `qwen2.5:7b` is not installed, so the pool uses the Linux profile and `qwen2.5:3b`.

`pytest` does not need Ollama. The CLI also runs with Ollama absent: rules still answer, and anything with no rule returns `escalate_paid` instead of calling out.

## Usage

```bash
brain ask "Who gets unowned leads?"
brain decide "They asked for a price on WhatsApp"
brain triage-lead '{"owner": null, "country": "ZA", "practice": true, "patients_per_month": 120, "setting": "medical"}'
brain assign "turn off the HighLevel workflow"
brain report --hq 10 --whatsapps 1500 --sales 1
brain ingest
```

`triage-lead` prints JSON: `hq`, `calendar` (`closer sales calendar` or `walkthrough webinar` or `none`), and `owner`.

Owner rules: a lead that already has an owner stays with that owner; a lead with no owner goes to Erich; a buyer goes to Davide. No SA price is written into the result. Optimum is the aesthetics panel. Neuro is the medical panel. US outreach is email only.

`report` builds the daily skeleton from the standing targets: 20 HQ bookings, 2,000 WhatsApps, 2 sales. Pass actuals when you have them. Missing actuals stay blank.

`ingest` rebuilds `vault/` from `sources/notes`. Pass `--raw` only when a dump with `memory/*.txt` is on disk; that path runs `scripts/build_brain.py` and `scripts/build_decision_model.py` under `BRAIN_EXPORT`. Those scripts are the original builders, with the export root taken from the environment. They call Ollama and expect the raw files the manifest describes. `raw/` was not shipped: the manifest says it was not redacted.

## Vault

Open `vault/` as an Obsidian vault. `Start here` is the map. Topic notes such as `standing-rules` and `team` are indexes. The long fact logs are dated notes under each topic folder, so the original wikilinks still resolve. Each fact keeps its `_source_` line.

## Open gaps

These are copied from `decision-model.md`. The CLI marks them as needing Davide rather than guessing.

- No explicit rule on decision-maker versus employee, budget or finance readiness, or timeline as HQ signals.
- Whether Davide's 9 Nov "book directly when they seem high quality" relaxes the over-100-patients-a-month gate, or keeps it.
- Aesthetics leads: whether Optimum-panel leads (no patient-count concept) use the same 100-a-month gate.
- US leads: no evidence of which sales calendar or closer handles US bookings. US outreach is email only.
- How to split new HQ bookings between Andries and Elmien beyond round robin, and when Davide's own calendar is used.
- Whether walkthrough-only past attendees who reply positively can go straight to a closer.

## Tests

```bash
pytest
```

Retrieval, the triage rules, and host fallback are covered. Ollama is replaced with a fake transport. A privacy scan fails the run if an email, phone number, or secret shape shows up in the markdown or JSON.

## Privacy

Redacted before this tree was committed:

- The US phone number on the Anthony Polenski line in `other` (replaced with `[phone]`).
- Bare mailbox locals with no domain: staff first-name mailboxes, the physio closer mailbox, the company sender, and two finance inboxes (replaced with `[email]`).

No API keys or bearer tokens were in the notes. Slack user IDs (for example `U06TXP9D7BR`) and HighLevel contact ids stay. No whole fact was dropped; the contact detail inside the fact was replaced.
