---
title: "Smartbot research and competitor learnings"
tags: [medwave, brain, smartbot, research, ads]
source: "Smartbot daily research in CEO inputs 1–6 Nov 2026; content-bot briefs; ad_quality_ranking_2026-11-01.md; competitor_pricing_matrix_2026-11-05.md; MedWave_Buyer_Profile_2026-11-01.pdf (aggregates only)"
date: 2026-11-18
privacy: "no lead or customer names, phones, emails, HighLevel contact IDs, or deposit-by-person details"
---

# Research and competitor learnings

Durable findings from Smartbot's 1–6 Nov 2026 research runs. Creative briefs went to Content bot via Master Control, not to Davide. Nothing below is a go-live approval.

Related: [[Smartbot/Smartbot]] · [[Smartbot/Improvement Log]] · [[Smartbot/Meta ads compliance watchlist]] · [[Smartbot/CEO input history]]

## How to judge ads

Quality is **cost per BDR-booked salesperson appointment**, not cost per lead. Rankings from 25–31 Oct 2026 (built 1 Nov, read-only) and later 30-day windows should be read with that definition. Ads with fewer than 5 matched HighLevel leads are directional only. One "bought" stage in the 1 Nov file was flagged unverified.

Source: `ad_quality_ranking_2026-11-01.md` (raw copy, including the per-lead CSV with contact IDs, is in `Smartbot/confidential/`).

### 25–31 Oct quality snapshot (1 Nov file)

| Ad | CPL rank (of 13 ads with Meta leads) | Quality rank (cost per booked) | Verdict |
|---|---|---|---|
| Booth Call – BiB | 1 ($6.69) | 1 ($40.14; $53.52 without the unverified sale) | Cheap and books. Best ad that week |
| Booth Call – BOOTH | 2 ($9.32) | 2 ($46.58, n=2) | Cheap and booked 1 of 2. Directional |
| Mashup Russel (RT form) | 3 ($10.58) | none: 0 booked (1 cancelled) | Cheap leads that did not book |
| Alne Static 2 (RT form), Legal-flagged | 4 ($13.31) | 6 ($146.43, 1 of 8 booked) | Cheap leads, weak booking |
| Support-Stranded (RT web) | 5 ($14.83) | 3 ($103.81, 2 of 7 booked, 1 attended) | Average CPL, better quality |
| 9Things Advantage+ (TOF) | 6 ($15.51) | none: 0 of 6 booked | Cheap leads that did not book |

Doctor and GP campaigns in the same week sat at about **$156–$349** per booked appointment. Renew Wellness (ZAR account) was excluded because it is a client campaign, not MedWave SA.

By 6 Nov (30 days to 5 Nov, Meta Lead Report 2026-11-06): Booth BiB was still cheapest at **$29.49** per booked call (12 booked / $354). The one practitioner-testimonial ad in the doctor funnel, Mashup Russel, was **$75.44** per booked call (6 booked / $453), versus $127.27 (9Things Website Guide) and $121.75 (Support-Stranded). That is one ad with 6 bookings — a direction, not proof that stories beat other formats. The other ad in that set (Alne Static 2, $73 per booked call) was a claims-flagged static paused on 5 Nov.

A 2 Nov weekly table (26 Oct–1 Nov) in `/workspace/medwave/smartbot_weekly/` used the same quality definition. Caveat recorded there: 70 of 123 HighLevel leads in that window were Meta-attributed; 53 had no ad attribution, and 9 of 20 salesperson bookings sat in the unattributed group.

## What long-running competitor ads actually sell

From Meta Ad Library scrapes (2–6 Nov), the B2B equipment ads that stay up longest usually do **not** sell the device in the ad:

- A low-pressure **practice planning call** or a **free live practitioner session** (2 Nov: Medical Spa Supply carousel 90 days, LIT Method recovery room 178 days, Complete Concussion workshop 571 days, Moxie timeline 133 days). MedWave's nav still said "Book a Sales Call".
- **Launch support** for a new room or partner (3 Nov: Renu Light, Contour Launch Lab, Nuvibody B2B, Rejuvn coaching).
- A **partner or provider programme** with non-cash benefits (4 Nov: Kineon Partner Program, 98 days, 8+ variants).
- **Multi-site / commercial procurement** (4 Nov: MericanGroup, 100 days).
- **Install-day proof** (4 Nov: Fitness Equipment Ireland carousel, 119 days).
- A stated **what happens next** — named person plus a time-boxed call (5 Nov: Nuvibody, Vital Red Light, Recovery Outlet, Red Light Wellness, Luxlight).
- Device-led **practitioner walk-through** and education-funnel PDFs (6 Nov: formats from Cryo By Coco and HBOT Revolution, used as format references only).

## What not to copy (RED)

Recorded across 2–6 Nov research, and aligned with [[Smartbot/Meta ads compliance watchlist]]:

- Guarantees, pay-per-show, $0 financing, income or payback maths, "wear it and it works".
- Invented doctor or vet advertorials; patient "walking again" stories.
- Revenue numbers inside testimonials (including a cited competitor figure of $53,900/month — do not copy).
- Cash referral commissions in ads or templates. Competitors were seen paying 8–15% (Infraredi, Onyx, Restore) and recruiting distributors. Old SA HighLevel templates that still promised cash referral fees were flagged to retire. No live commission test without Davide.
- A provider risk noted on 6 Nov: a centre was running MedWave-named health claims plus a "starting at" price for 269 days. Format may be studied; claims and price must not be copied.

## Creative briefs sent to Content bot

All routed through Master Control. Legal and QA gates stay in force. Davide approves go-live.

| Date | Angle | Creatives | Gate / outcome in surviving files |
|---|---|---|---|
| 2 Nov | Booking step as a practice planning call / free live session | C1 SA carousel, C2 SA recovery room, C3 (blocked), C4 SA timeline (name `SB-C4-SA-Timeline` so it is never confused with the banned 1 Nov C04) | C1, C2, C4 passed QA (19/19 images) and Legal; C4 post-text still needed explicit Legal clearance; C3 not runnable while `/cpd-event/` said "[Topic to confirm]". All blocked on a live HighLevel booking URL + Davide's yes. |
| 3 Nov | Launch support, group walkthrough, e-book form, owners-only line | C1 Partner Launch Kit in ads; other 3 Nov angles as briefed | Brief sent. |
| 4 Nov | Partner programme, multi-site, install-day proof, learning library | C1 provider network (non-cash benefits); C2 2+ locations qualifier; C3 install-day shots with consent | Brief sent. |
| 5 Nov | Click-to-WhatsApp B2B (SA) and unused-equipment education + PBM e-book | C1 device-hero click-to-WA (destination = HighLevel-connected SA WhatsApp number, not a community group); C2 education loop, SA first, USA wellness-only variant | **HOLD** until the 10-minute booking path is live. Source ads were cited by Ad Library id in the brief; revenue maths not to be copied. |
| 6 Nov | Practitioner stories as process-proof, plus win-back | C1 "One consult hour" device-led walk-through (SA); C2 Practice Story 2-page process PDF + practice-type e-book (no outcomes or revenue numbers); C3 "Three rooms, three practitioners" peer-quote carousel (needs ≥3 consenting customers; Janae); C4 "what's new" win-back email, not an ad, owners unchanged | New briefs that day. Do not launch more B2B volume ads until the 10-minute path exists. Confirm Option B disclosure on the lander and every clip before the 10 paused Practitioner Stories cuts go live (a text fetch did not show the line). |

Beat Booth BiB ($40.14 in the 1 Nov week; $29.49 in the 30-day window to 5 Nov) or say why not. Judge a practitioner-story creative only once it has at least 10 booked calls.

## Practitioner proof gap (6 Nov)

Buyers want a case from a business like theirs (Mixology: 42% ranked case studies most influential; PRIZMA: 40.2% valued similar businesses; Ipsos: 56% said case studies still matter). All 10 clips on the Practitioner Stories page came from one interview. Next proof should come from a different practice type (gym or studio, physio, wellness) with written paid-ad consent.

## Pricing context (not for ads)

Public pages checked 5 Nov (`competitor_pricing_matrix_2026-11-05.md`, 15 rows):

- InfraMed SA published no prices. Red Light Rising published ZAR prices for handhelds and a clinical spotlight (R5,599 to R18,299), offered free onboarding and a 365-day trial, and showed full-body panels only in GBP (Advantage 900: £1,725).
- Full-body clinic panels in SA were listed at about **R25k to R93.5k** (Suele, Global Trade Mart, Derma Roller, Solid O2, ReGenX). That is far below MedWave's **R250k to R300k** packages.
- Visible finance/rental: botthms R3,666.50/m interest-free and rent-to-own over 6 to 24 months; The Rental Guys R1,700/m. **Hutton Medical publicly listed the MedWave Neuro-100S at R115,000**, so a MedWave price was already online.
- Missing from those pages: InfraMed prices, Red Light Rising ZAR panel prices, VAT basis on several sites, and install or training terms except botthms (Gauteng install).

Lead-facing price rules remain those in [[no-sa-pricing-before-call]] and [[monthly-prices-only]]. This matrix is context only.

## Buyer profile (1 Nov, aggregates only)

Smartbot built a read-only buyer profile and list (1 Nov). The PDF cover states aggregates only. The CSV contains personal details and stays in `Smartbot/confidential/`.

From the profile summary:

- 410 unique buyers merged across HighLevel, MedX-related Gmail and Stripe: **250 confirmed paid** (213 SA, 37 USA), 58 contract only, 102 CRM-won only.
- **63%** of SA paid buyers were aesthetics, GP or wellness.
- Median SA lead-to-close **44 days** (n=98).
- Typical SA buyer described as a small, owner-run aesthetics, GP or wellness practice that came in through Meta, was set by a BDR and closed at around R250k.
- Blocker recorded: MedX itself was not opened, so product, price and finance fields were mostly blank and the list was partial. A MedX buyer export (or approved access) was requested.

## Weak campaigns and attribution (2 Nov, directional)

Cited from `smartbot_2026-11-02.md` and `weak_campaigns_pause_proposal_2026-11-02.md`: RT LANDERS $472.09 / 1 lead (optimising for landing-page views, 0 HighLevel-attributed bookings); Nurses US $390.16 / 5 leads but only 5 landing-page views from 87 clicks (tracking or page problem); Andries Gym Box already paused (69 WhatsApp chats at $3.85 each). This was a review list, not a kill list, because booking attribution was not live. Ad-to-booking attribution was blocked by website forms not storing `utm_ad_id`, uneven tags, a new Instant Form not mapped, and an expired US Facebook token. Pixel audience sizes of "20" were an API placeholder, not a real size.

A 3 Nov Meta decision pack (waiting on Davide) said pausing 8 weak ad sets would free about $180/day of about $430/day.

## Ad Library coverage and software

- 2 Nov: compliance check also recorded the Master Ads account as ACTIVE, 39 live ads, a history of 36 disapprovals, and a Meta balance owed (see the watchlist for the morning figure; it had risen by evening).
- 5 Nov: Meta 262 ads / 15 queries; LinkedIn 39 details; GATC reachable; TikTok login wall. Files: `/workspace/adlib/d1105/`.
- 6 Nov: Meta 504 unique ads / 30 queries; LinkedIn 13 details; same GATC/TikTok limits. Files: `/workspace/adlib/d1106/`.
- 6 Nov research also noted a third-party blog claiming a July 2026 Meta health-policy rewrite, while Meta's Transparency page still dated 27 Dec 2024. **No change** was made to MedWave rules or the 2 Nov watchlist on the back of that.
- Recommendation repeated 5–6 Nov: **no new software** beyond the HighLevel Conversation AI add-on for the 10-minute path.

Back to [[Smartbot/Smartbot]].
