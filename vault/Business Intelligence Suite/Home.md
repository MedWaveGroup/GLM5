---
title: "Business Intelligence Suite - Home"
tags: [medwave, bi-suite, cpd]
bi_type: index
updated: 2026-11-12
refreshed_sast: "2026-11-12 11:14"
source: "refresh_bi_suite.py (Google Sheets + read-only HighLevel export)"
privacy: "no emails or phone numbers"
---
# Business Intelligence Suite

MedWave's BI layer in the brain. It starts with the CPD audience: everyone on the CPD attendee and registrant lists Davide shared on 12 Nov 2026, merged, de-duplicated and matched to HighLevel (read-only).

> [!warning] Pricing rule
> Every doctor in this suite is on a CPD list. **No pricing at all** until Davide changes the rule. `cpd - attended` does not unlock pricing. Full prices are never quoted. See [[Business Intelligence Suite/Rules - CPD Pricing|Rules - CPD Pricing]].

> [!danger] Barefoot list is data only — never contact
> Davide, 12 Nov 2026 14:34 SAST: doctors who appear **only** on the Barefoot Bytes spreadsheet must never be texted, WhatsApped or emailed by any bot or outreach send. They stay in this suite and in the merged Google Sheet as reference data. Contact details are not stored in this vault.
>
> This does **not** apply to the 73 doctors who are also on a webinar attendee or did-not-attend list; those leads may be reached. Unassigned webinar leads are assigned to Erich.

## Headline numbers (12 Nov 2026 11:14 SAST)

| Measure | Value |
|---|---|
| Unique doctors (master) | 11702 |
| Attended the 10 Nov CPD webinar | 333 |
| Registered, did not attend | 559 |
| Barefoot list only | 10810 |
| Attended and in HighLevel | 318 (95%) |
| Attended and booked | 102 (31%) |
| Attended and sold | 1 |
| HighLevel CPD contacts not on the sheets | 601 |

## What the numbers say

- 312 doctors with contact details and 21 name-only attendees participated in the webinar.
- 318 out of 333 attendees are categorized as HighLevel.
- 309 attendees have received at least one message, and 170 have responded.
- 102 attendees are booked (31%), and 1 has made a purchase.

_Summary written by Ollama qwen2.5:3b on 127.0.0.1 (numbers checked against the facts)._

## Notes

- [[Business Intelligence Suite/CPD Attendees Dashboard|CPD Attendees Dashboard]] — counts by event, specialty, province, owner, booked, DND, pricing hold
- [[Business Intelligence Suite/Pipeline & Conversion|Pipeline & Conversion]] — attended → contacted → replied → booked → sold
- [[Business Intelligence Suite/Follow-up Priorities|Follow-up Priorities]] — who to call next, by bucket
- [[Business Intelligence Suite/Rules - CPD Pricing|Rules - CPD Pricing]] — the binding pricing and contact rules for this audience
- [[Business Intelligence Suite/Data Dictionary|Data Dictionary]] — every field, where it comes from
- [[Business Intelligence Suite/How to Refresh|How to Refresh]] — rebuild from the Sheet and HighLevel

Full contact details live only in the Google Sheet "CPD Attendees – Merged Master (12 Nov 2026)" (https://docs.google.com/spreadsheets/d/1jE3XJMNVNTua6klve-s_wTQN-tPV3o_tsnF2QnKR6RM/edit) and in `/workspace/bi-suite/confidential/` on the box, never in this vault.

Back to [[Start here]].
