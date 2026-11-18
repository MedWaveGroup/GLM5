---
title: "Data Dictionary"
tags: [medwave, bi-suite, cpd]
bi_type: reference
updated: 2026-11-12
refreshed_sast: "2026-11-12 11:14"
source: "refresh_bi_suite.py (Google Sheets + read-only HighLevel export)"
privacy: "no emails or phone numbers"
---
# Data Dictionary

Suite: [[Business Intelligence Suite/Home|Home]] · [[Business Intelligence Suite/CPD Attendees Dashboard|CPD dashboard]] · [[Business Intelligence Suite/Pipeline & Conversion|Pipeline]] · [[Business Intelligence Suite/Follow-up Priorities|Follow-ups]] · [[Business Intelligence Suite/Rules - CPD Pricing|Rules]] · [[Business Intelligence Suite/Data Dictionary|Data dictionary]] · [[Business Intelligence Suite/How to Refresh|Refresh]]

Fields on the Master tab of the Google Sheet (and the xlsx). Fields marked † are confidential and appear only in the Sheet and `/workspace/bi-suite/confidential/`, never in this vault.

| Field | Meaning | Source |
|---|---|---|
| master_id | Stable ID for one unique doctor in this build (BI00001…) | merge |
| title, first, last | Name from the highest-ranked source row (attended > registered > Barefoot) | sheets |
| practice | Organisation / practice (webinar lists only) | Webinar sheets: Organization |
| specialty | Raw specialty or position | Barefoot: Speciality; webinar: Position |
| specialty_group | One of 14 groups; regex rules first, then Ollama qwen2.5:3b for leftovers (cached) | refresh script |
| work_type | Barefoot Type Work | Barefoot |
| email †, other_emails † | Normalised emails (lower case, trimmed) | sheets |
| phone †, other_phones † | SA numbers normalised to +27 | sheets |
| city, province | Home area; province from area text, landline code, or HighLevel state | sheets + HL |
| attendance_status | Attended / Attended (name only, unverified) / Registered - did not attend / Barefoot list | sheets |
| events, event_count, lists_count | Every list the doctor is on; count of attended webinars; count of lists | merge |
| contactId, other_contactIds | HighLevel contact ID(s) matched | HL |
| hl_match | email, mobile, or name (unique, low confidence) | match |
| owner | HighLevel assigned user | HL assignedTo |
| bdr | BDR split on the attendee sheet or HL "bdr - x" tag | sheets + HL |
| dnd | HL DND flag, any active DND channel, or opt-out tag | HL |
| cpd_tags, sequence_tags, relevant_tags | CPD tags; N1/B1–B5 tags; CPD, sequence, booked and davide-bot-outreach tags | HL |
| last_inbound, last_outbound | Latest inbound / outbound message (SAST), from the newest two conversations | HL conversations |
| next_appointment, last_appointment, appointments, showed, no_shows | Appointments excluding cancelled (SAST) | HL appointments |
| booked, booked_basis | yes if live appointment, booked tag or stage, or BDR note says booked | HL + sheets |
| sold | Opportunity in a Deposit Received / Cash Collected / Sold-Closed / Financing connected / Existing customer stage | HL opportunities |
| opportunities, opportunity_value | Pipeline: stage (status); summed value (mostly R0) | HL |
| funnel_stage | Sold > Booked > Replied > Contacted > In HighLevel > Not in HighLevel | derived |
| follow_up_bucket | Priority bucket; see Follow-up Priorities | derived |
| pricing_hold, pricing_hold_reason | Always YES on this audience; reason list | rule |
| bdr_notes † | Notes from the BDR split tabs | Webinar Attendee list |
| conflicts | Differences found while merging (names, emails, mobiles, specialty, shared contact) | merge |
| possible_duplicate_of | Other master IDs with the identical full name (not merged) | merge |
| dup_reason, source_count, sources | Why rows were merged; how many; which sheet/tab/row | merge |
| enrichment | ok / partial / not fetched for HL appointments and messages | refresh |

## Dedupe order

1. Same normalised email. 2. Same normalised SA **mobile** (+27 6/7/8; landlines and switchboards are never a key). 3. Fuzzy name (≥ 0.88 similarity) within the same named practice. A shared email or mobile with a clearly different name is **not** merged; it is flagged in `conflicts`. Identical full names with no shared contact are flagged in `possible_duplicate_of`.

## Sources

| Sheet | Tab | Rows | Used as |
|---|---|---|---|
| Barefoot-List-Match-Workbook | Barefoot List Full | 11100 | all Barefoot doctors (Working, Work Type and Area tabs are views of the same rows) |
| Barefoot-List-Match-Workbook | Match List / MedWave List Full | 344 / 7124 | reference only |
| Webinar registrants - did not attend (balance) | Did not attend (balance) | 559 | registered, did not attend |
| Webinar Attendee list (found in Drive) | Sheet1 + BDR tabs | 333 | attended (312 with contact details, 21 name-only) |

## Barefoot never-contact rule

Doctors whose `attendance_status` is `Barefoot list` (Barefoot source and not on either webinar list) must never be contacted. This rule is enforced from the CSV `barefoot_no_contact_2026-11-12.csv` and is recorded in [[Business Intelligence Suite/Rules - CPD Pricing|Rules]]. Contact details stay in the Google Sheet and in `/workspace/bi-suite/confidential/`, never in this vault.
