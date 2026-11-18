---
title: "How to Refresh"
tags: [medwave, bi-suite, cpd]
bi_type: runbook
updated: 2026-11-12
refreshed_sast: "2026-11-12 11:14"
source: "refresh_bi_suite.py (Google Sheets + read-only HighLevel export)"
privacy: "no emails or phone numbers"
---
# How to Refresh

Suite: [[Business Intelligence Suite/Home|Home]] · [[Business Intelligence Suite/CPD Attendees Dashboard|CPD dashboard]] · [[Business Intelligence Suite/Pipeline & Conversion|Pipeline]] · [[Business Intelligence Suite/Follow-up Priorities|Follow-ups]] · [[Business Intelligence Suite/Rules - CPD Pricing|Rules]] · [[Business Intelligence Suite/Data Dictionary|Data dictionary]] · [[Business Intelligence Suite/How to Refresh|Refresh]]

Everything runs on the box except the HighLevel pull, which runs read-only on Davide's Mac (the token never leaves the Mac and is never printed). Ollama stays on loopback (127.0.0.1:11434); no tunnels.

1. **Sheets** — download the source sheets onto the box with `DownloadFile` (Google Drive) into `/workspace/bi-suite/confidential/src/` as `sheet1_barefoot.xlsx`, `sheet2_webinar.xlsx`, `sheet3_webinar_attendees.xlsx`.
2. **HighLevel (read-only, on the Mac 4e5e8a44)**
   - `python3 /Users/davide/medwave/bi_export/export_contacts.py` (all contacts, ~12 min)
   - `CopyToBox` `contacts_full.jsonl` → `/workspace/bi-suite/confidential/hl/`
   - on the box: `python3 /workspace/bi-suite/scripts/match_highlevel.py` (writes `hl/enrich_ids.txt`), `CopyFromBox` it to `/Users/davide/medwave/bi_export/`
   - on the Mac: `python3 enrich_contacts.py` (appointments + last messages; resumable), then `CopyToBox` `enrich.jsonl` and `meta.json`
3. **Rebuild** — `python3 /workspace/bi-suite/scripts/refresh_bi_suite.py --sheet-url <master sheet url> --vault "/home/box/glm5/vault"`
   - Writes the xlsx, per-tab CSVs for the Google Sheet (confidential), and these notes. Add `--no-ollama` to skip the local model.
   - A privacy scan aborts the vault write if an email address or phone number appears.
4. **Google Sheet** — rewrite the tabs of "CPD Attendees – Merged Master (12 Nov 2026)" from `confidential/sheet_*.csv`.
5. Never commit `/workspace/bi-suite/confidential/`; it is git-ignored.
6. **Barefoot never-contact list.** After a refresh, rebuild `/workspace/team/outreach-control/barefoot_no_contact_2026-11-12.csv` (every Barefoot-only row, including unmatched phones and emails). Run `/workspace/team/outreach-control/sync_barefoot_no_contact.sh` to update the box watcher copy, then CopyFromBox the same CSV to `/Users/davide/medwave/lead-watcher/barefoot_no_contact.csv` on Mac `4e5e8a44-7882-4b4d-9240-e17d496c7766`. Senders reload the file when its mtime changes; kickstart `com.medwave.lead-watcher` only if `guards_1112.py` itself changed. Do not message Barefoot-only doctors and do not write DND or tags to HighLevel for them.

Ollama work in this build: 0 specialty label calls (cached in `/workspace/bi-suite/cache/specialty_labels.json`), 1 summary call.
