---
title: "Start here"
tags: [medwave, brain, moc]
source: "vault compile"
date: 2026-11-09
---

# Start here

This is the MedWave manager brain for Master Control. Answer from a rule or from this vault before any paid model is called.

## Order

1. A deterministic rule or a lookup in [[standing-rules]] and [[decision-model]].
2. A local Ollama model on loopback (`brain ask`, `brain decide`). Davide's Mac uses `qwen2.5:7b`. The Linux box uses `qwen2.5:3b`.
3. The `escalate_paid` flag, with a reason. A human flag means Davide, not a bigger model.

The full 13-stage Ollama-first flow, including send gates, is in the repo at `docs/PROCESS_FLOW.md`. The short operating knowledge base is `docs/KNOWLEDGE_BASE_TRUNCATED.md` (PDF: `docs/MedWave_Knowledge_Base_2026-11-12.pdf`). Helper scripts live in `tools/ollama_helpers/`.

## Map

- [[index]] — every note
- [[decision-model]] — how Davide decides, and the HQ rubric
- [[standing-rules]] — rule cards and the fact log
- [[team]] — one note per person
- [[lead-handling]] · [[objections]] · [[booking-and-calendars]] · [[targets-kpis]]
- [[products-positioning]] · [[channels]] · [[bots]] · [[davide-decisions]]
- [[other]] · [[workspace-index]]

## Commands

- `brain ask "question"`
- `brain decide "situation"`
- `brain triage-lead '{...}'`
- `brain assign "task"`
- `brain report`
- `brain ingest`
- `/workspace/team/outreach-control/ask_brain.sh "question"` — objection notes only, then qwen2.5:3b

Local first, tokens last.
