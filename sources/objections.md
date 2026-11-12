---
title: "Objections"
tags: [medwave, brain, objections]
source: "LEADS: Objection bot playbook v1.4; Outreach Control notes 11-12 Nov 2026; Davide Duranti 12 Nov 2026 06:21 and 10:21–10:25 SAST"
date: 2026-11-12
---

# Objections

One short note per objection, so a local Ollama model can pull only the relevant card instead of a whole playbook. Hard rules that apply to every reply live in [[guardrails]]. Use `/workspace/team/outreach-control/ask_brain.sh '<question>'` or `brain ask '<question>'`.

Related: [[standing-rules]] · [[lead-handling]] · [[davide-decisions]] · [[leads-objection-bot]] · [[index]] · [[Start here]]

## Guardrails and new rules

- [[guardrails|Standing guardrails for every objection reply]]
- [[already-a-provider-nearby|Already a MedWave or provider in my area]]
- [[cancellation-is-not-a-price-decline|A cancellation is never a price decline]]
- [[patient-price|Patient price line, confirmed patients only (monthly amounts; 11 Nov full-price line SUPERSEDED 12 Nov 10:21)]]
- [[cpd-no-pricing|CPD-list doctors get no pricing until they attend an event]]
- [[monthly-prices-only|Lead-facing prices are monthly amounts only]]
- [[send-windows|24-hour skip for blasts and reactivation; 1-hour re-touch; no repeated wording]]

## Playbook objections (v1.4, plus later Davide rules)

- [[ghosting]]
- [[not-interested]]
- [[not-now-timing]]
- [[finance-interest]]
- [[budget-too-expensive]]
- [[need-to-think-partner]]
- [[no-space]]
- [[science-doubt]]
- [[too-busy-no-staff]]
- [[low-patient-volume]]

## How to retrieve

- Objection-only (preferred, small context): `/workspace/team/outreach-control/ask_brain.sh "<question>"`
- Whole vault: `brain ask "same question"` (BM25 over the vault, then qwen2.5:3b on loopback).
