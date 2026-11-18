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
- [[lead-handling]] · [[objections]] · [[decisions]] · [[booking-and-calendars]] · [[targets-kpis]]
- [[products-positioning]] · [[channels]] · [[bots]] · [[davide-decisions]]
- [[other]] · [[workspace-index]]
- [[Business Intelligence Suite/Home|Business Intelligence Suite]] — CPD audience dashboard, pipeline, follow-up priorities and the CPD no-pricing rule
- [[Smartbot/Smartbot|Smartbot]] — continuous-improvement findings (Improvement Log, research, Meta ads watchlist, fleet/blockage, CEO input history). Paused since 6 Nov 2026 19:11 SAST

## Commands

- `brain ask "question"`
- `brain decide "situation"`
- `brain triage-lead '{...}'`
- `brain assign "task"`
- `brain report`
- `brain ingest`
- `/workspace/team/outreach-control/ask_brain.sh "question"` — objection notes, standing rules and watcher decision cards, then qwen2.5:3b

Local first, tokens last.
