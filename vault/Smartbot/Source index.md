---
title: "Smartbot source index"
tags: [medwave, brain, smartbot]
source: "Vault ingest 18 Nov 2026. Filenames only for confidential raw files."
date: 2026-11-18
privacy: "lists filenames only; no personal details"
---

# Source index

This folder is a sanitized digest. Raw files that contain lead or customer names, phones, emails, HighLevel contact IDs, or deposit-by-person details are **not** in the public repo. They were copied to `vault/Smartbot/confidential/` on the box, which is gitignored (`**/confidential/`).

Related: [[Smartbot/Smartbot]]

## Tracked notes (this repo)

- [[Smartbot/Smartbot]]
- [[Smartbot/Improvement Log]]
- [[Smartbot/Research and competitor learnings]]
- [[Smartbot/Meta ads compliance watchlist]]
- [[Smartbot/Fleet and blockage findings]]
- [[Smartbot/CEO input history]]
- [[Smartbot/Source index]]

Already in the vault, linked rather than copied: [[decision-model]] (includes the Davide decision playbook). The full playbook remains at `/workspace/context/DAVIDE_DECISION_PLAYBOOK.md` on the box.

## Confidential copies placed at ingest (gitignored)

These are copies of surviving Smartbot-authored or Smartbot-cited sources. Reference them by filename only.

- `smartbot_2026-11-01.md`
- `smartbot_2026-11-02.md`
- `smartbot_2026-11-03.md`
- `smartbot_2026-11-04.md`
- `smartbot_2026-11-05.md` (engine-room copy; same text as the CEO-data 5 Nov input)
- `smartbot_ceo_input_2026-11-05.md`
- `smartbot_ceo_input_2026-11-06.md`
- `content-bot-brief-2026-11-02.md`
- `content-bot-brief-2026-11-03.md`
- `content-bot-brief-2026-11-04.md`
- `content-bot-brief-2026-11-06.md`
- `weekly-top3-research-brief-2026-11-04.pdf`
- `MEDWAVE_META_ADS_WATCHLIST_2026-11-02.md`
- `ad_quality_ranking_2026-11-01.md`
- `lead_quality_2026-11-01.csv` (contains HighLevel contact IDs)
- `competitor_pricing_matrix_2026-11-05.md`
- `competitor_pricing_matrix_2026-11-05.csv`
- `MedWave_Buyer_Profile_2026-11-01.pdf`
- `buyers_list.csv` (contains names, businesses, HighLevel contact IDs)
- `README_2026-11-02.md` (weekly ad-performance note)
- `medwave_ads_7d_2026-10-26_to_2026-11-01.csv`

## Missing at ingest (not on the box, not in medwave-bot-backup as of 18 Nov 2026 15:29 SAST)

The pending Notion-row folder `/workspace/team/improvement-log-pending/` was gone. Smartbot's 5–6 Nov CEO inputs cited these filenames, among others:

- `sweep_2026-11-05_0830.md`, `sweep_2026-11-05_1430.md`
- `sweep_2026-11-06_0830.md`, `sweep_2026-11-06_1030.md`, `sweep_2026-11-06_1230_closure.md`, `sweep_2026-11-06_1430.md`
- `fleet_2026-11-06_0910.md`, `fleet_2026-11-06_1110.md`, `fleet_2026-11-06_1700.md`
- `hq_2026-11-06_1300.md`, `hq_2026-11-06_1500.md`
- `research_2026-11-05.md`, `research_2026-11-06.md`
- `creative_brief_2026-11-05.md`, `creative_brief_2026-11-06.md`
- `leak_positive_to_booking_2026-11-04.md`
- `r1_reply_speed_2026-11-05_1410.md`, `owner_alert_spec_2026-11-05.md`, `bulk_wa_exclusion_filter_spec_2026-11-05.md`
- `slack_numbers_draft_2026-11-05_1715.md`, `2026-11-05_1630_pacing.md`, `2026-11-06_1715_pacing.md`
- earlier pending sweeps such as `sweep_2026-11-02_calendar_reactivation.md`

The 6 Nov CEO input also cited ops files (`replies_2026-11-06_1700.md`, `replies_carry_2026-11-06_1700.md`, `scores_2026-11-06.md`, ledger dumps). The replies-carry files were still under `/workspace/engine-room/replies/` and were read for the Garden Route 869 count, but they contain personal details so they were **not** copied into this public repo. They were also **not** copied into `confidential/` in this pass (they are Engine Room reply logs, not Smartbot-authored packs). A copy can be added later if needed.

## Looked at and not ingested as Smartbot notes

- `/workspace/context/DAVIDE_DECISION_PLAYBOOK.md` — already represented by [[decision-model]]; not duplicated.
- `/workspace/medwave/reports/` daily Meta lead PDFs, decision packs, compliance checks, go-live checklists — cited where Smartbot used them, but many are Reporting Bot / Meta Ad Account bot outputs; not copied as Smartbot notes.
- `/workspace/creatives/smartbot/` and dated `*_smartbot-c1-*` folders — Content bot drafts from Smartbot briefs, not re-homed here.
- `/workspace/strategy/install_backlog_2026-11-05.md`, `refund_call_list_2026-11-05.md`, `low_sales_doc_2026-11-05.txt` — authorship not clearly Smartbot; skipped.
- No standalone "SSOT" or "subscriptions" file was found. The single sales-feed proposal lives in the 1 Nov input and in [[Smartbot/Improvement Log]].

Back to [[Smartbot/Smartbot]].
