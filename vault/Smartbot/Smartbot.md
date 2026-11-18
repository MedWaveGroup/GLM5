---
title: "Smartbot"
tags: [medwave, brain, smartbot, moc]
source: "Smartbot vault ingest 18 Nov 2026; surviving box files under /workspace/reports/ceo_data, /workspace/engine-room/ceo-report/inputs, /workspace/briefs, /workspace/meta_guides, /workspace/medwave/quality, /workspace/buyers, /workspace/strategy"
date: 2026-11-18
privacy: "no lead or customer names, phones, emails, HighLevel contact IDs, or deposit-by-person details"
status: "paused since 6 Nov 2026 19:11 SAST"
---

# Smartbot

Id: `ba891246-c4dc-4f07-ba66-6ff33b39c74a`.

MedWave's continuous-improvement bot. It monitors company systems, identifies inefficiencies, proposes improvements, and reports to [[master-control|Master Control]] for action. It cites sources, does not invent data, and is **read-only** on every system: no sends, no HighLevel edits, no Notion writes, no spend, and no publishing.

Related: [[bots]] · [[bots/smartbot]] · [[decision-model]] · [[standing-rules]] · [[index]] · [[Start here]]

## Role and reporting

- Reports only to Master Control (`189da52e-5641-4f83-accc-c8a4ad5668f1`). Standing rule from 3 Nov 2026: Smartbot never messages Davide directly with stats, reports, FYIs or questions. If Davide asks for something, the result also goes to Master Control.
- Improvement Log rows were held in box files under `/workspace/team/improvement-log-pending/` after the Notion block-limit freeze, instead of being written to the Notion database.
- Outputs that still exist on the box are cited from the notes below. Raw copies that contain personal details live only in `Smartbot/confidential/` on the box (gitignored; this repo is public).

## Status (as of 18 Nov 2026)

**Paused.** Davide, 6 Nov 2026 19:11 SAST: "Pause all tasks across all bots we are spending too much on tokens. Only do the outreach I asked for earlier to new leads coming into the system or leads responding to texts. Stop everything else." Master Control reconfirmed on 8 Nov 2026 19:51 SAST: do not resume until Davide asks himself.

- Last live company-data pull: 6 Nov 2026, about 17:46–17:50 SAST (late fleet / HQ audit).
- Last update sent to Master Control: 6 Nov 2026 CEO input, about 19:33–19:40 SAST.
- This vault folder was first written on 18 Nov 2026 after Davide asked for the data to move into the GitHub Obsidian brain. Smartbot had not written to the vault before that. Routines stay paused; this ingest is not a restart of sweeps or research.

Paused routines (as of 6–8 Nov): blockage sweep, daily research, daily CEO PDF input, and team check-in.

## Notes in this folder

- [[Smartbot/Improvement Log|Improvement Log]] — proposals from 1–6 Nov, with owner, status and source
- [[Smartbot/Research and competitor learnings|Research and competitor learnings]] — ad, competitor, buyer-profile and lead-quality findings
- [[Smartbot/Meta ads compliance watchlist|Meta ads compliance watchlist]] — 2 Nov digest of the VCA Meta guides, plus the 10-question pre-launch test
- [[Smartbot/Fleet and blockage findings|Fleet and blockage findings]] — sweeps, HQ counts and corrections, by date
- [[Smartbot/CEO input history|CEO input history]] — sanitized history of the daily CEO PDF inputs
- [[Smartbot/Source index|Source index]] — surviving source filenames, including gitignored raw files

## Corrections to keep in view

These were reported to Master Control on 6 Nov 2026 and supersede earlier wording in the same day's drafts:

- The `{phone}` / `{email}` placeholder flag (72 messages at the 08:30 sweep) was treated as a **suspected export or render discrepancy** after a 09:18 live check: 14 sampled cached IDs returned resolved live bodies. Do not drive workflow edits on the 72 alone. Source still on file: `smartbot_ceo_input_2026-11-06.md` §3.4.
- The **5.8–5.9% failure rate** (64/1,080 at 15:30, reproduced) is **all-channel**, not WhatsApp-only.
- **HQ qualification** for the 6 Nov bookings is **unknown / unverified**. An earlier line that "0 of 3" were proven-qualified (>100 patients/month) should not be treated as a verified fact.
- A Garden Route invite bulk total of **869** appears in the 6 Nov replies-carry files. Smartbot later corrected the composition to **869 = 414 + 266 + 52 + 137** when reporting to Master Control. The original fleet file that labelled those components is missing from the box (see [[Smartbot/Source index|Source index]]).
- A related consumer-match count was corrected to **23, not 25**. The 6 Nov 17:50 fleet, as summarized in the CEO input, also reported **8** "Just tried you" hits that day to consumer-excluded contacts.
- A staff-alert claim was **dropped**.
- One 6 Nov ledger deposit's test status, the legality of the US SMS nurture sends, and the CIPC deadline were all left **unverified**.

## Already in the vault (do not duplicate)

- How Davide decides, including the playbook principles: [[decision-model]] (sourced in part from `/workspace/context/DAVIDE_DECISION_PLAYBOOK.md`).
- Hard rules: [[standing-rules]], including [[bots-report-to-mc]], [[hq-definition]], [[no-sa-pricing-before-call]], [[buyer-rule]], [[us-email-only]], [[owned-leads-stay]], [[unowned-leads-erich]], [[opt-out]].
- The short bot stub: [[bots/smartbot]].

Back to [[Start here]].
