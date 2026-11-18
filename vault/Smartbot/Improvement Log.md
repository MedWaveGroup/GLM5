---
title: "Smartbot Improvement Log"
tags: [medwave, brain, smartbot, improvement-log]
source: "Surviving Smartbot CEO inputs and briefs, 1–6 Nov 2026. Original pending Notion-row files under /workspace/team/improvement-log-pending/ were not on the box at ingest (18 Nov 2026)."
date: 2026-11-18
privacy: "no lead or customer names, phones, emails, HighLevel contact IDs, or deposit-by-person details"
---

# Smartbot Improvement Log

Pending Notion writes were held in `/workspace/team/improvement-log-pending/` after the block-limit freeze. Notion itself had **no rows dated 5 or 6 Nov 2026**. The pending folder was **missing from the box** (and from the 18 Nov 15:29 SAST medwave-bot-backup sync) when this note was written, so entries below are reconstructed only from surviving daily inputs and briefs. Status is as last recorded on 6 Nov 2026, after which Smartbot was paused.

Related: [[Smartbot/Smartbot]] · [[Smartbot/Research and competitor learnings]] · [[Smartbot/Fleet and blockage findings]] · [[Smartbot/CEO input history]]

Status key: **Proposed** = sent to Master Control, no closure recorded in surviving files. **Open** = still unresolved as of 6 Nov. **Corrected** = later evidence changed the finding. **Hold** = blocked on a dependency.

## 1 Nov 2026

| Date | Finding | Recommended fix | Owner | Status | Source |
|---|---|---|---|---|---|
| 2026-11-01 | Daily numbers disagree across four places | Single sales feed from the MedX ledger plus a product field (SSOT) | Master Control + Ian | Proposed. No standalone SSOT file was found on the box at ingest. | `smartbot_2026-11-01.md` |
| 2026-11-01 | 27 automated messages went to 9 contacts after STOP (31 Oct) | "Reply 1" / STOP must suppress all marketing; fix and test before the next morning send | Sterrenberg | Open as of later opt-out work (see 2–4 Nov). | `smartbot_2026-11-01.md` |
| 2026-11-01 | USA inbound unread and the HighLevel Facebook integration expired; Stripe quiet | Recover US email/Facebook path; do not use SMS until consent is settled | Anthony + Messaging Performance | Open; later tightened to email-only (Anthony). | `smartbot_2026-11-01.md` |
| 2026-11-01 | Pixel audience sizes showing "20" | Check before trusting retargeting; later found to be an API placeholder, not a real size | Meta Ad Account bot | Open / explained 2 Nov. | `smartbot_2026-11-01.md`; `pixel_audiences_2026-11-02.md` (cited) |
| 2026-11-01 | Neuro-100S page references 1, 2 and 6 are wrong | Fix the page | Website owner | Proposed. | `smartbot_2026-11-01.md` |
| 2026-11-01 | Practitioner referral-fee test used by competitors (Celluma $500/order, Joovv 8%) | Research only; Davide decides any live test | Radar / Davide | Proposed. Later (4 Nov) flagged as RED: no referral-commission action without Davide, and old SA templates promising cash referral fees should be retired. | `smartbot_2026-11-01.md`; `smartbot_2026-11-04.md` |
| 2026-11-01 | Lead with monthly cost in the first ad or message (Technolase/Pulse pattern) | Davide decides | Davide | Proposed. | `smartbot_2026-11-01.md` |
| 2026-11-01 | Paid 30-day rental credited to a later purchase, as a reactivation offer | Davide decides | Davide | Proposed. | `smartbot_2026-11-01.md` |
| 2026-11-01 | LinkedIn test in one B2B vertical ($0 spend since 1 Aug) | Davide decides | Davide | Proposed. | `smartbot_2026-11-01.md` |
| 2026-11-01 | Rank ads on BDR-vetted bookings, not CPL alone | Agree a tagging spec, then rank | Francois + Meta Ad Account bot | Proposed; quality ranking file built the same day. | `smartbot_2026-11-01.md`; `ad_quality_ranking_2026-11-01.md` |

## 2 Nov 2026

| Date | Finding | Recommended fix | Owner | Status | Source |
|---|---|---|---|---|---|
| 2026-11-02 | Long-running B2B equipment ads sell a low-pressure planning call or a free practitioner session, not the device. Site nav still says "Book a Sales Call". | Reframe to a practice planning call; brief C1–C4 sent to Content bot | Content bot → QA → Legal; Davide approves go-live | C1, C2 and C4 SA passed QA (19/19 images) and Legal, with C4 post-text still needing explicit Legal clearance; C3 blocked because `/cpd-event/` still had a placeholder. All were blocked on a live HighLevel booking URL and Davide's yes. | `smartbot_2026-11-02.md`; `content-bot-brief-2026-11-02.md` |
| 2026-11-02 | Weak campaigns in the 22 Oct–2 Nov window: RT LANDERS expensive with 0 HighLevel-attributed bookings; Nurses US clicks not reaching the page; Andries Gym Box already paused | Review, not a kill list (booking attribution was not live) | Meta Ad Account bot / Davide | Proposed. | `smartbot_2026-11-02.md`; `weak_campaigns_pause_proposal_2026-11-02.md` (cited) |
| 2026-11-02 | Six live RT LANDERS ads landed on QA-failed pages; health terms in URLs/UTMs; some ads had no UTMs; Instant Form thank-you used a sold-out discount claim | Compliance clean-up; Account Quality check; see the watchlist | Legal, QA, Meta Ad Account bot, Davide (site clean-up + Meta balance) | Open as of 2 Nov. | `smartbot_2026-11-02.md`; [[Smartbot/Meta ads compliance watchlist]] |
| 2026-11-02 | First-touch gap: 165 of 246 SA inbound leads (67%, 20 Oct–2 Nov) had no HighLevel welcome within 24 hours. Cause described as no trigger, not send failures. | Welcome trigger on website/FB/event capture | Sterrenberg | Later **corrected** by Master Control at 19:35 SAST: the remaining uncontacted set was cut sharply after Messaging Performance and Outreach bot checks; nurture D1 went out with Davide's go-ahead. The welcome trigger fix itself was still open. | `smartbot_2026-11-02.md` (including the 19:35 corrections) |
| 2026-11-02 | "Opted out" tag did not exist in SA HighLevel, so the 1 Nov rule was not live | Create the tag, keep opted-out contacts, never message them | Sterrenberg | Open; completion not confirmed in files Smartbot could see that day. | `smartbot_2026-11-02.md`; [[opt-out]] |
| 2026-11-02 | Setters logged few HighLevel WhatsApps and 0 HighLevel calls or SMS in the window; work was happening on personal phones; no setter linked to an SA number | Get setter activity onto HighLevel numbers and logs | Francois / Sterrenberg | Open. | `smartbot_2026-11-02.md` |
| 2026-11-02 | Content, Legal and QA were working from more than one rules file, causing re-work | One shared rules file that Legal and QA both keep current | Master Control, Legal, QA, Content | Proposed. | `smartbot_2026-11-02.md` |

## 3 Nov 2026

| Date | Finding | Recommended fix | Owner | Status | Source |
|---|---|---|---|---|---|
| 2026-11-03 | Competitors headline launch support, not just the device | Use the Partner Launch Kit in ads and on calls; no revenue guarantees (brief C1) | Content bot + Meta Ad Account bot | Briefed. | `smartbot_2026-11-03.md`; `content-bot-brief-2026-11-03.md` |
| 2026-11-03 | "See it running" group walkthroughs run for a long time in competitor ads | Fixed weekly group walkthrough (closers already had walkthrough seats 2–6 Nov) | Closers / Content | Proposed. | `smartbot_2026-11-03.md` |
| 2026-11-03 | Nerve Endings e-book ad: spend and 0 leads | Switch to an Instant Form with a practitioner qualifier, or pause | Meta Ad Account bot | Proposed. | `smartbot_2026-11-03.md` |
| 2026-11-03 | Booth Call BiB is the quality benchmark | Test a "business owners only, not a treatment booking" line against it | Content / Meta Ad Account bot | Proposed. | `smartbot_2026-11-03.md` |
| 2026-11-03 | Meta decision pack: pausing 8 weak ad sets would free about $180/day of about $430/day | Davide yes/no on the pack | Davide; Meta Ad Account bot | Waiting on Davide as of 3 Nov. | `smartbot_2026-11-03.md` |
| 2026-11-03 | Opt-out backfill and "not interested" / stop-requested tags were not fully blocking workflows and bulks | Enforce DND and suppression before 2,000/day outreach | Sterrenberg | Open. | `smartbot_2026-11-03.md` |
| 2026-11-03 | Unowned-contact plan v2.1 and a 589-contact reactivation pool | Davide sign-off, then Sterrenberg loads and owners message | Davide; Sterrenberg; owners | Waiting on sign-off as of 4 Nov carry. | `smartbot_2026-11-03.md`; `smartbot_2026-11-04.md` |
| 2026-11-03 | Website form leads arriving in mailboxes instead of HighLevel with an owner and an instant welcome | Inbound speed-to-lead into HighLevel | Sterrenberg | Open. | `smartbot_2026-11-03.md` |
| 2026-11-03 | Installation Schedule not used; booth heat tests above the panel rating | Book dated installs; hold booth installs/ads until a retest at 30°C or below | Janae, Ian | Open (retested concern still on 4 Nov). | `smartbot_2026-11-03.md`; `smartbot_2026-11-04.md` |

## 4 Nov 2026 (public holiday)

| Date | Finding | Recommended fix | Owner | Status | Source |
|---|---|---|---|---|---|
| 2026-11-04 | Partner-programme ads run for a long time in the Ad Library (Kineon pattern) | Test "Join the MedWave provider network" with non-cash benefits only (install and training, provider-map listing, launch kit, webinars) | Content bot + Meta Ad Account bot; Janae/Ian confirm inclusions | Brief C1 sent. | `smartbot_2026-11-04.md`; `content-bot-brief-2026-11-04.md` |
| 2026-11-04 | Multi-site buyers exist (competitor "commercial procurement only" ads; an existing customer had asked about multiple stores) | "2+ locations" qualifier and a numbered-steps form (brief C2); buyers to Davide | Content bot; Davide for buyers | Briefed. | `smartbot_2026-11-04.md` |
| 2026-11-04 | Install-day proof is a durable competitor format | Add a consent tick and a 4-shot list to installs (brief C3) | Janae, Content bot | Briefed. | `smartbot_2026-11-04.md` |
| 2026-11-04 | Provider map showed 307 businesses (228 SA, 78 USA, 1 ZW) as at 4 Nov | Replace "450 / 400+ / 280+" style counts in claims (claims-audit #24) | Legal bot, Ian | Proposed. | `smartbot_2026-11-04.md` |
| 2026-11-04 | Competitors pay 8–15% referral commission and recruit distributors; old SA templates still promised cash referral fees | Retire those templates. No live commission programme without Davide | Davide only | RED, proposed. | `smartbot_2026-11-04.md` |
| 2026-11-04 | Reply-to-booking leak: of 15 positive replies that day, 13 had no human reply and none received a booking link or slot | Owners to offer a call (two slots + link); no SA pricing in chat | Master Control → named owners | Open; became the 5 Nov research focus. | `smartbot_2026-11-04.md`; `leak_positive_to_booking_2026-11-04.md` (file missing at ingest) |
| 2026-11-04 | Eddie's discovery calendar showed 0 business-hour slots; Elmien's Friday was empty | Fix open hours or remove the broken calendar from booking paths | Sterrenberg; Francois for Elmien follow-up | Still unfixed on 5–6 Nov. | `smartbot_2026-11-04.md`; `smartbot_ceo_input_2026-11-05.md` |
| 2026-11-04 | Reactivation pool sized at 589 SA contacts with an unworked positive reply (tiers A 191 / B 233 / C 165) | Owners start messaging after sign-off | Davide sign-off; owners | Proposed. | `smartbot_2026-11-04.md` |
| 2026-11-04 | 6,535 SA contacts with no owner; high-quality/R75k scan listed 77 unowned contacts | Ownership plan v2.1 waiting on Davide sign-off | Davide; Sterrenberg | Open. On 6 Nov Davide ruled unassigned leads go to Erich immediately and owned leads stay. | `smartbot_2026-11-04.md`; `smartbot_ceo_input_2026-11-06.md` |

## 5 Nov 2026

| Date | Finding | Recommended fix | Owner | Status | Source |
|---|---|---|---|---|---|
| 2026-11-05 | Reply speed is the conversion lever (HBR 2011; Optifai). Same-day typed positives: median 5.9 minutes to a human reply (6 of 7 answered) but **0 of 7** were offered two slots plus a booking link within 10 minutes. A 39-lead recheck at 11:05 still had 36 open and 0 newly booked. | Add daily Slack KPIs (median minutes; % offered two slots + link). Build a 10-minute path on HighLevel Conversation AI (Suggestive mode first; books into the owner's calendar; never reassign; buy-intent goes to a human). Pilot one week, then decide on Auto-Pilot. | Sterrenberg (build) + LEADS: Outreach Control (rules/copy) + Davide (cadence-pause and AI spend) + Master Control (Slack KPI) | Spec written (`owner_alert_spec_2026-11-05.md`, missing at ingest). **Still unbuilt** as of 6 Nov. | `smartbot_ceo_input_2026-11-05.md` R1–R2, top 10 #2 and #10 |
| 2026-11-05 | Creative C1: click-to-WhatsApp B2B (SA), device hero. Creative C2: unused-equipment education loop + PBM e-book. Do not copy competitor revenue maths. | Draft via Content bot after the 10-minute path is live; Legal review; SA first, USA wellness-only variant for C2 | Content bot → Legal → Meta Ad Account bot | Briefed; **HOLD** pending the 10-minute path. | `smartbot_ceo_input_2026-11-05.md`; creative brief 5 Nov (missing at ingest) |
| 2026-11-05 | Competitors state what happens next (named person + time-boxed call) | Add a thank-you / B2B lander block once the 10-minute promise can be kept | Content / Website | Proposed, gated on R1. | `smartbot_ceo_input_2026-11-05.md` R5 |
| 2026-11-05 | SA ad P2 `1421049469958614` still showed as active in the Ad Library on a 5 Nov scrape (claims-audit row) | Pause or fix, confirmed via Legal + Meta Ad Account bot | Legal bot + Meta Ad Account bot via Master Control | Still live on the 5 Nov scrape. | `smartbot_ceo_input_2026-11-05.md` R7 |
| 2026-11-05 | Garden Route / Fancourt bulk hit closed-lost and CVS contacts (incident count recorded as 8 closed-lost, 2 CVS) | Apply bulk exclusion filters (closed-lost, CVS, DND, providers, booked, buy-intent owners) before the next wave | Sterrenberg; Outreach Control pre-flight | Spec drafted (`bulk_wa_exclusion_filter_spec_2026-11-05.md`, missing at ingest). Still open 6 Nov, when a "Just tried you" consumer leak was also confirmed. | `smartbot_ceo_input_2026-11-05.md`; `smartbot_ceo_input_2026-11-06.md` |
| 2026-11-05 | Erich website-lead SMS workflow still said "red light therapy" | Fix the wording | Sterrenberg (asked about 14:19) | Proposed. | `smartbot_ceo_input_2026-11-05.md` |
| 2026-11-05 | HighLevel Billing and WhatsApp template/wallet pages 404; SMS still paused (footer); one insufficient-funds fail that day | Clear billing/wallet and payment method; keep SMS paused until the footer is right | Sterrenberg | Carried into 6 Nov. | `smartbot_ceo_input_2026-11-05.md` |
| 2026-11-05 | Elmien follow-up SMS alerts were hitting Twilio 30008 (open High from Notion, 2 Nov) | Switch alerts to WhatsApp/email/HighLevel task. Francois interim: Elmien works HighLevel by hand. Francois owns Elmien calendar follow-up (Sterrenberg 17:24). Ignore Eddie for BDR tracking. | Francois; Sterrenberg | Open. | `smartbot_ceo_input_2026-11-05.md` |
| 2026-11-05 | SigningHub "MEDWAVE RSA – COLLECTIONS" awaiting Davide; Surfside FICA ~30 days unanswered; CIPC due Fri 6 Nov; move OTPs off the company inbox (a payment was confirmed) | Davide signs / chases; Rachel/Ian support | Davide; Rachel/Ian | Open. CIPC deadline later marked **unverified**. | `smartbot_ceo_input_2026-11-05.md` |
| 2026-11-05 | Daily numbers and blockers belong on Slack, not Notion (Davide 4 Nov) | Master Control to post the Slack list; Smartbot drafted a 17:15 list | Master Control | Drafted. | `smartbot_ceo_input_2026-11-05.md` |
| 2026-11-05 | No new software beyond the HighLevel AI add-on | Do not buy another tool for the 10-minute path | — | Standing recommendation through 6 Nov. | `smartbot_ceo_input_2026-11-05.md` R8; `smartbot_ceo_input_2026-11-06.md` R10 |

## 6 Nov 2026

| Date | Finding | Recommended fix | Owner | Status | Source |
|---|---|---|---|---|---|
| 2026-11-06 | Practitioner-voice is the thinnest ad supply. One practitioner-testimonial ad in the doctor funnel cost $75.44 per booked call (6 booked / $453, 30 days) vs $127.27 and $121.75 for two other doctor-funnel ads. Booth BiB remained best at $29.49 (12 booked / $354). Ten Practitioner Stories cuts were built but paused. | Briefs C1–C4: consult-hour video; Practice Story PDF; peer-quote carousel (needs at least three consenting customers before live); non-ad win-back email. Do not launch more B2B volume ads until the 10-minute path exists. Confirm Option B disclosure on the lander and every clip before the 10 cuts go live (a text fetch did not show the line). | Content bot → Legal → Meta Ad Account bot; Janae for more practitioners | **New briefs today**; 5 Nov C1/C2 still on HOLD. | `smartbot_ceo_input_2026-11-06.md`; `content-bot-brief-2026-11-06.md` |
| 2026-11-06 | All live Practitioner Stories proof on the site came from one practitioner interview | Add gym/studio and physio stories with written paid-ad consent | Janae | Proposed. | `smartbot_ceo_input_2026-11-06.md` R2 |
| 2026-11-06 | `{phone}` / `{email}` placeholders: 08:30 sweep flagged 72 messages | Do **not** drive workflow edits on the 72 alone | — | **Corrected** 09:18: 14 sampled cached IDs returned resolved live bodies; treat as a suspected export/render discrepancy pending device verification. | `smartbot_ceo_input_2026-11-06.md` §3.4; `fleet_2026-11-06_0910.md` (missing at ingest) |
| 2026-11-06 | Context CSV exclusion does not gate the HighLevel "Just tried you" workflow; 8 consumer-excluded contacts were messaged that day | Ship HighLevel-side exclusion gates (consumer, closed-lost, CVS, DND, providers, booked, buy-intent) before the next JTY or bulk | Sterrenberg | Open. A related consumer-match count was later corrected to 23, not 25. | `smartbot_ceo_input_2026-11-06.md` §2.8 and §3.1 |
| 2026-11-06 | US nurture workflow still sent SMS on 6 Nov after Anthony's email-only ruling, including a testimonial without a disclaimer; a timezone SMS leak also re-fired | Consent gate or email-only swap, without turning workflows off; Legal on the testimonial | Sterrenberg + Legal bot; Anthony via Ian | Proposed. **US SMS legality left unverified.** | `smartbot_ceo_input_2026-11-06.md` §2.6; corrections to Master Control |
| 2026-11-06 | Outreach 1,113 / 2,000 by 17:15 (gap 887). Fail 5.8–5.9% all-channel (64/1,080 at 15:30, reproduced). Batch 005 sent 0 (template lookup empty + 51/52 mismatch; still 0 at 17:22). | Unblock Batch 005 (exact WhatsApp template ID + confirmed list) or formally drop the 2,000 chase for the day. Do not describe the fail rate as WhatsApp-only. | Sterrenberg + Francois + Outreach Control | Open at pause. | `smartbot_ceo_input_2026-11-06.md` |
| 2026-11-06 | Form field mapping: phone and email glued; email-as-first-name; short-code phones (repeat instances) | Fix capture mapping | Sterrenberg | Open. | `smartbot_ceo_input_2026-11-06.md` §3.5 |
| 2026-11-06 | Ledger showed new deposits/payments that were not yet marked won in HighLevel | Log and stage-win in HighLevel; hand confirmed sales to Janae onboarding. One earlier deposit remained internal-looking and was to be excluded from sale counts; its test status was later left **unverified**. A bank credit that only name-matched a closed-lost/DND contact was not on the ledger. | Rachel/Rozanne (ledger); Francois and setters (HighLevel); Ian cover | Proposed the same day. No closure recorded before the pause. | `smartbot_ceo_input_2026-11-06.md` §2.4–2.5 |
| 2026-11-06 | A financed equipment proposal draft had sat unsent for about 50 hours, plus aged company-inbox drafts | Inbox Manager to produce an age-sorted "drafts awaiting send" list; Ian/Francois triage while Davide was off | Ian; Inbox Manager | Open. | `smartbot_ceo_input_2026-11-06.md` |
| 2026-11-06 | Elmien's Wednesday calendar was closed, but a closer booking had been set for that Wednesday | Francois owns Elmien calendar follow-up; fix the off-calendar booking | Francois | Open. | `smartbot_ceo_input_2026-11-06.md` §3.7 |
| 2026-11-06 | Davide, about 12:23 SAST: unassigned leads go to Erich immediately; owned leads stay | Apply on capture and clear the unowned backlog | Francois / Sterrenberg | Ruled; implementation not confirmed in surviving files. | `smartbot_ceo_input_2026-11-06.md` §3.6; [[unowned-leads-erich]] · [[owned-leads-stay]] |

## Open High Notion backlog (mostly 1–2 Nov, still listed on 6 Nov)

These were already in Notion with status typically "Sent to Master Control" or Assigned, and were not new 5–6 Nov discoveries: SAHPRA live-series wording, Elmien SMS 30008, USA unread / expired Facebook token, WhatsApp wallet/templates 404, missing Opted-out tag, positive-reply backlog, claims guardrail, unsent company-inbox drafts, outreach volume, Facebook Instant Form welcome break, partner launch kit, Voice AI outbound, signed-unpaid chase, SOP drafts, empty Daily Department Reports, finance-from-first-touch, paid rental offer.

Notion database (reference only): https://app.notion.com/p/94f2edf3344f490ab5249570d7d6307e

Back to [[Smartbot/Smartbot]].
