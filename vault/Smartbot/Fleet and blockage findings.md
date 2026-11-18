---
title: "Smartbot fleet and blockage findings"
tags: [medwave, brain, smartbot, fleet, ops]
source: "Surviving Smartbot CEO inputs 1–6 Nov 2026 and engine-room replies-carry files. Original sweep/fleet/HQ markdown under /workspace/team/improvement-log-pending/ was not on the box at ingest (18 Nov 2026)."
date: 2026-11-18
privacy: "no lead or customer names, phones, emails, HighLevel contact IDs, or deposit-by-person details"
---

# Fleet and blockage findings

Dated operational findings from Smartbot sweeps, fleet audits and HQ counts. Names of leads and customers, contact IDs, and deposit-by-person details are omitted. Staff first names and bot names are kept.

The original 5–6 Nov sweep, fleet and HQ files were not on the box (or in the 18 Nov 15:29 SAST backup sync) when this note was written. Figures below come from the surviving CEO inputs that cited those files, plus the 6 Nov replies-carry files that are still under `/workspace/engine-room/replies/`.

Related: [[Smartbot/Smartbot]] · [[Smartbot/Improvement Log]] · [[Smartbot/CEO input history]] · [[hq-definition]] · [[targets]]

## Daily engine-room targets (for context)

From standing rules: 20 high-quality closer-calendar bookings a day, 2,000 outbound messages a day, 2 sales a day. HQ means a closer-calendar booking, not a walkthrough.

## 1 Nov 2026

- 58 closer bookings in 10 working days, about 5.8/day vs the 20 target. Most setters had 0 HighLevel WhatsApp sends.
- 16,081 SA contacts untouched 30+ days. Manual replies booked 4.8% vs automated 1.2%. Workflows not built; 6 SOPs still draft.
- 13 "signed, deposit pending" vs 12 "deposit made" in the 12–30 Oct window, unreconciled in places.
- 74 open Meta leads (Hazel 30, Eddie 31, 13 unowned).
- USA: 1,121 unread (newest then 5 Oct), Facebook integration expired in HighLevel, no US end-of-days.
- 20 installations outstanding, 1 refund request on record (29 Oct).
- 9-in-10 claim unevidenced (email to Rozanne 19:27).

Source: `smartbot_2026-11-01.md`.

## 2 Nov 2026

- HQ bookings: 13 of 20 made (Elmien 7, Andries 4, Karin 2). Closer calls next 14 days 29 (was 22). 1 deposit/win vs the 2/day target.
- Closer capacity 2–6 Nov: 22 one-to-ones booked, about 37 slots still open (Andries about 29, Elmien about 8; Elmien showed nothing on Wed 4 Nov — confirm).
- First-touch gap initially reported as 165 of 246 SA inbound leads (67%, 20 Oct–2 Nov) with no HighLevel welcome within 24 hours; 123 never had a successful HighLevel message; cause described as no trigger. **Master Control correction 19:35 SAST:** Messaging Performance cut the remaining catch-up to 114 by 16:20; Outreach bot found only 8 real uncontacted SA leads (others already worked, email-only, DND, tests, or out of market). Nurture D1 went out 17:50–18:14 with Davide's go-ahead: 6 delivered or read, 1 failed, 1 skipped. The welcome trigger fix was still open.
- Warm leads: first draft said 24 positive replies with no booking/human reply (10 waiting 24h+), only 2 of 30 positives booked. **Correction 19:35:** over 14 days there were 248 unbooked positive replies, 100 of them needing a person; 12 had waited 24h+ as of 17:15.
- Outreach: 1,067 of 2,000 sent, 89 failed (8.3%), 60 replies. SMS failing 34.6% (Twilio 30008). WhatsApp wallet: 1,513 "insufficient funds" failures 26 Oct–2 Nov.
- Overdue HighLevel SA tasks: 20 (not 15), 8 from 2025, 4 unassigned.
- Reactivation pool: 16,079 of 24,210 SA contacts (66.4%) inactive 30+ days; 11,350 WhatsApp-eligible, but only 1,312 explicitly B2B-tagged, so screening comes first. Cost estimate about $33/day at 1,000/day.
- USA: 5 emails, 0 replies, no appointments; last Stripe charge 17 Oct; 1,121 unread; 0 Facebook leads in 14 days (expired token).
- Sales-feed mismatch: a ledger deposit and a HighLevel win did not match; marked unverified.
- "Opted out" tag still missing in SA HighLevel.

Source: `smartbot_2026-11-02.md`, including the 19:35 Master Control corrections.

## 3 Nov 2026

Surviving 3 Nov input is thinner in the research/top-10 extract than a full fleet dump. Items carried into the top 10 that day included: opt-out enforcement on a 28-contact backfill and "not interested" / stop-requested suppression; unowned-contact plan v2.1 and a 589-contact reactivation pool waiting on Davide; inbound website forms still landing in mailboxes; installation pipeline and booth heat (tests 38–40°C vs a 25°C ambient panel rating; paid-not-installed figure cited as R1.53m on 3 Nov); blank first-name merges and WhatsApp wallet failures; USA still with no sale since Sep 2025.

Source: `smartbot_2026-11-03.md`.

## 4 Nov 2026 (public holiday; closers/BDRs off)

- Reply-to-booking leak to 16:14: 15 positive replies, 13 with no human reply, 0 offered a booking link or slot. Several buy-intent conversations were still open after hours (owners included Elmien, Erich, Eddie, Andries). Lead names omitted here; see the confidential CEO input.
- Eddie's discovery calendar showed 0 business-hour slots Thursday and Friday. Elmien had only a short Thursday window and 0 Friday. Erich had 32 slots each day.
- SA pricing was sent in writing after the 14:27 no-pricing-before-call rule (two documented cases). Package wording also differed between quotes.
- Reactivation pool: 589 SA contacts with an unworked positive reply (A 191 / B 233 / C 165); largest books with Elmien 110, Erich 107, Andries 82; Davide held 32 tier-A.
- Unowned SA contacts: 6,535. Plan v2.1 waiting on Davide. High-quality/R75k scan: 77 unowned contacts.
- Outreach round-one wording had waited 15h+ for Francois/Sterrenberg approval as of 08:30.
- Stripe MedWave Group LLC: 0 charges and 0 disputes that day; a $500 invoice still open.
- Booth heat hold remained in force until a retest at 30°C or below.
- HQ bookings that day (from the 5 Nov "changed since yesterday" table): 2 vs 20. Outreach 1,279 sent, 185 failed.

Sources: `smartbot_2026-11-04.md`; `smartbot_ceo_input_2026-11-05.md` comparison table.

## 5 Nov 2026

- HQ bookings: **11–12 created / about 10–11 live** vs 20 (rose from 7/6 at 14:10 → 11 at about 16:12 → 12 at about 16:31). 1 no-show. Setters: Erich 4, Karin 3, Hazel 2, Michael 2. Zero as setters: Eddie, Sterrenberg, Elmien, Andries. Walkthroughs 4–5, counted separately.
- Outreach: **1,964** lead-facing verified in HighLevel by about 16:31 (gap 36; 1,744 delivered). 220 failed (11.2%); 1 insufficient-funds. Francois's 586-pack was largely logged by 15:1x (599 bulk to 585 contacts; 102 failed). SMS still paused (footer). Email ≤90/hr Mailgun. WhatsApp wallet/billing 404 still open.
- Typed positives that day: median **5.9 minutes** to a human reply (6 of 7 answered) but **0 of 7** offered two slots plus a booking link. 39-list recheck 11:05: **36 still open, 0 newly booked**. Outreach Control 19:30: 14 Positive / 1 Buyer that day; 65 held.
- Garden Route / Fancourt bulk incident: 8 closed-lost and 2 CVS contacts hit. Exclusion-filter spec drafted the same day.
- Eddie's calendar still had 0 business-hour slots. Elmien Friday still empty. Sterrenberg ruled Eddie is not a BDR for tracking (17:24); Francois owns Elmien calendar follow-up.
- USA: email-only until SMS consent (Anthony). Unread still about 1,245; newest Facebook DM unread March 2026.
- Installation Schedule still empty vs the 2 booked + 2 completed/day KPI.
- Finance/compliance carry: SigningHub collections pack awaiting Davide; Surfside FICA ~30 days; CIPC due 6 Nov (later marked unverified); OTP routing off the company inbox still open.

Sources: `smartbot_ceo_input_2026-11-05.md` (citing `sweep_2026-11-05_0830.md`, `sweep_2026-11-05_1430.md`, pacing and reply-speed files — those source files were missing at ingest).

## 6 Nov 2026 (Davide day off; last live pull about 17:46–17:50 SAST)

HQ checks through the day, as later summarized for Master Control:

| Time (SAST) | What was reported | Caveat |
|---|---|---|
| 13:00 | 2 created, 4 scheduled (1 no-show) | Qualification unverified |
| 15:00 | 3 created (Michael 2, Erich 1) | Qualification unverified |
| 17:50 late fleet | **3 created / 20** on 8 HQ calendars | Engine Room pacing counted **4** if Karin's own calendar was included. Setter vs a 3-each split: Erich 1, Michael 2, Eddie 0, Hazel 0. Booked-for-today 4 (1 no-show; 3 unmarked after the slot). Zero marked "showed". **Qualification unknown / unverified** — do not use an earlier "0 of 3 proven-qualified" line as a verified fact. |

Other 6 Nov findings:

- Outreach **1,113 / 2,000** by 17:15 (gap 887; end-of-day projection about 1,127). Fail **5.8–5.9% all-channel** (64/1,080 at 15:30, reproduced) — not WhatsApp-only. Manual WhatsApp vs quota was thin (Erich 28/88, Michael 11/68, Hazel 8/68, Eddie 1/68). **Batch 005 sent 0** (API/template failure 14:04; still 0 at 17:22).
- Afternoon window 12:10–17:05: **4 positives, 0 booked**. Carry file: **50 positives waiting 24h+** (was 44 at noon). Owner split in the carry file included unknown 11, Elmien 8, Andries 8, Eddie 7, Erich 6, Hazel 6.
- Placeholder `{phone}` / `{email}`: 08:30 flagged 72 messages. **Fleet 09:18 correction:** 14 sampled cached IDs returned resolved live bodies. Treat the 72 as a suspected export or render discrepancy. Do not drive workflow edits on that count alone.
- "Just tried you" consumer leak confirmed: **8** consumer-excluded contacts hit that day. Context CSV exclusion did not gate the HighLevel workflow. A related consumer-match count was later corrected to **23, not 25**.
- Garden Route invite bulk: **869** recipients in `replies_carry_2026-11-06_1700.md` (and the 12:00 carry file). Smartbot later corrected the composition to **869 = 414 + 266 + 52 + 137** when reporting to Master Control. The fleet file that labelled those components is missing.
- A staff-alert claim was **dropped**.
- Ledger showed new deposits/payments not yet marked won in HighLevel. One earlier deposit was to be excluded from sale counts pending clarification; its test status was left **unverified**. A bank credit that only name-matched a closed-lost/DND contact was not on the ledger.
- US nurture still sent SMS after Anthony's email-only ruling, including a testimonial without a disclaimer; a timezone SMS leak also re-fired. **Legality left unverified.**
- Form mapping issues: phone and email glued; email-as-first-name; short-code phones.
- Installation Schedule still empty vs the daily KPI.
- SigningHub collections pack still awaiting Davide; CIPC had been described as due that day (deadline **unverified**); Surfside FICA still open; Stripe LLC 0 new charges since 5 Nov, 0 disputes; a $500 invoice still open.

Sources: `smartbot_ceo_input_2026-11-06.md` (citing `sweep_2026-11-06_0830.md`, `1030.md`, `1230_closure.md`, `1430.md`, `fleet_2026-11-06_0910.md`, `1110.md`, `1700.md`, `hq_2026-11-06_1300.md`, `hq_2026-11-06_1500.md` — those files missing at ingest); `/workspace/engine-room/replies/replies_carry_2026-11-06_1700.md`.

## After 6 Nov 19:11 SAST

No further fleet or blockage sweeps. Smartbot paused on Davide's instruction, reconfirmed 8 Nov. This 18 Nov vault ingest is not a new data pull.

Back to [[Smartbot/Smartbot]].
