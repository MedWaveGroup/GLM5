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

## Map

- [[index]] — every note
- [[decision-model]] — how Davide decides, and the HQ rubric
- [[standing-rules]] — rule cards and the fact log
- [[team]] — one note per person
- [[lead-handling]] · [[booking-and-calendars]] · [[targets-kpis]]
- [[products-positioning]] · [[channels]] · [[bots]] · [[davide-decisions]]
- [[other]] · [[workspace-index]]

## Commands

- `brain ask "question"`
- `brain decide "situation"`
- `brain triage-lead '{...}'`
- `brain assign "task"`
- `brain report`
- `brain ingest`

Local first, tokens last.
