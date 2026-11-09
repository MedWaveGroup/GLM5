---
title: "Davide decision model"
tags: [medwave, brain, decision-model]
source: "facts_tagged.json (memory, transcripts, context docs); DAVIDE_DECISION_PLAYBOOK.md §A"
date: 2026-11-09
---

# How Davide decides

Related: [[notes/davide-decisions]] · [[notes/standing-rules]] · [[notes/booking-and-calendars]] · [[notes/targets-kpis]] · [[notes/index]]

## 1. Priorities (from the playbook's ten principles, written by Master Control from his rulings)

**1. The engine room comes first, and it's measured in numbers.** Marketing → appointments → sales → operations, aiming for 40 sales a month (2 a day), 20 high-quality bookings a day and 2,000 outbound messages a day. "Inputs create outputs."
**2. Bots report to Master Control, not to Davide.** He redirected bots to MC at least 9 times:
**3. Do the work first, then show him the finished product and the reason for it.**
**4. Decide fast and close the loop, and don't re-ask.** He answers in one line and moves on:
**5. He accepts commercial claims risk in SA when he believes the claim is true, but holds a few hard lines.** He overrode Legal or QA 14 times in the log, mostly on claims and consent:
**6. His word counts as the fact source, but it gets logged.** He supplies facts directly and expects bots to use them:
**7. Give, give, give, take (GGGT) is the default for all follow-up.** Three pieces of value, then one ask. Demos are offered in messages but booked on a call with a salesperson.
**8. Chase people until they confirm, and hold managers accountable.**
**9. Real, accurate, high-quality brand visuals.**
**10. Keep spend lean and keep things running: test and iterate, don't pause.**

## 2. Standing rules and the evidence behind them

- **Buyer rule: anyone with buying intent (price questions, "I want to start", ready to buy) is routed to Davide himself, not back to a setter or closer.**
  - Evidence (undated, transcript:LEADS: Context bot#pos168 (assistant)): "owner Erich) asked 'How much is it may I ask?' at 11:42. Erich hasn't replied yet. Pricing goes to Davide, and he handles leads with buying intent himself. He's off today, so Ian or Francois for anything urgent. She has had the practitioner proof and the brochure. Please hold her automated nurture."
  - Evidence (undated, transcript:LEADS: Outreach Control#pos937 (assistant)): "nt video message. Bot sent nothing; logged ROUTED_URGENT_SALESPERSON. Please route buying intent to Davide per his buyer rule, not back to a setter. First clarify business/device purchase vs personal weight-loss use; current evidence is ambiguous. Owner Andries Yj7mjEZBYBC5CqF1dNL2 unchanged, Erich"
- **No SA pricing in writing before a sales call. Price questions get a call offer, not a number.**
  - Evidence (2026-11-05, memory:journal): "5 Nov 2026 ~16:17 SAST: MP Francois response report (contactIds) ready; Slack draft t791s3115; Slack file F0CFAM8A0QL uploaded pending share to C0CDZHCBCH5 thread 1793871379.265259 on Davide send. Buyer L6MDCKJ42pYLi2zWFLnL (Michael, how much per session) routed to Davide — no SA pricing before call."
  - Evidence (2026-11-05, memory:journal): "5 Nov 2026 ~16:27 SAST: Michael typed SA price ranges ("R100k to a few million ex VAT") to buyer contactId jIVGRyu6Gdq263ApTLpw (Sterrenberg owner, "how much does it cost?") — breaches Davide rule no SA pricing before sales call; buyer should go to Davide."
- **Elmien is contacted on Slack only (never WhatsApp/SMS/email from the bots).**
  - Evidence (2026-11-05, memory:profile): "As of 5 Nov 2026, buy-intent urgent chases still go Slack + WhatsApp to the salesperson — except Elmien, who gets Slack only (never WhatsApp) for follow-up nudges."
  - Evidence (2026-11-06, memory:profile): "As of 6 Nov 2026 ~12:20 SAST, Davide ruled that when Master Control sees failures like unanswered positive replies, missed targets or stale leads, it must escalate and hold people accountable directly on Slack without asking him first, using bold text, warning emojis and @-tags to get attention (Elmien still Slack only; names-of…"
- **Owned leads keep their owner; never reassign. Unowned leads go to Erich.**
  - Evidence (2026-11-06, memory:profile): "As of 6 Nov 2026, standing rule that any lead with no clear owner goes to Erich straight away; leads that already have an owner stay with that person."
  - Evidence (2026-11-06, memory:shared_profile via Master Control): "As of 6 Nov 2026 ~12:23 SAST, Davide ruled that leads with no clear owner (unassigned in HighLevel) are assigned to Erich by default, immediately; leads that already have an owner still stay with that owner."
- **Unowned leads default to Erich.**
  - Evidence (2026-11-06, memory:journal): "6 Nov 2026 ~12:37 SAST: Francois response report 30m posted to thread 1793871379.265259 (msg 1793961439.257959): today 39 replies/31 contacts (pos 32, q 4, neg 1, STOP 1, auto 1); 1 new since 12:06 (12:28 KWzOvdEi6ujixRy4f4LS Andries WA "2 uur vandag" ack for 14:00 call). Open no human: DA7VRfNAppBIZsAoG1hl (~6h), 5BmYAdx0g0M192…"
- **US outreach is email only (no SMS/WhatsApp consent in the US).**
  - Evidence (2026-11-05, memory:shared_profile via Master Control): "As of 5 Nov 2026 ~12:06 SAST, Anthony Polenski ruled that no US texts/SMS may go out without proof of active SMS consent; older US leads and the current US web form have no consent field, so US outreach is email-only until an SMS consent checkbox and matching HighLevel field are added."
  - Evidence (2026-11-05, memory:profile): "As of 5 Nov 2026 ~12:06 SAST, Anthony Polenski ruled that no US texts/SMS may go out without proof of active SMS consent; older US leads and the current US web form lack a consent field, so the US outreach test is email-only until an SMS consent checkbox and matching HighLevel field are added."
- **Optimum panel only in aesthetics settings; Neuro in medical settings.**
  - Evidence (2026-11-07, memory:shared_profile via LEADS: Outreach Control): "As of 7 Nov 2026 15:50 SAST, Davide ruled MedWave product positioning: offer the Optimum panel only in aesthetics contexts (spas, aesthetic/skin practices) and the Neuro (Neuro100S) panel in any medical context."
  - Evidence (undated, transcript:LEADS: Outreach Control#pos928 (assistant)): "n you approved with one line added that points her to the Optimum as the best fit for an aesthetics practice, and it still has no pricing. I've also saved two things for future replies. I'll reply to responding leads without checking with you first, and I'll suggest the Optimum for aesthetics leads"
- **MedWave never pays leads' travel or accommodation for events.**
  - Evidence (2026-11-06, memory:shared_profile via LEADS: Outreach Control): "As of 6 Nov 2026 22:30 SAST, Davide ruled MedWave never covers leads' travel or accommodation for events (e.g. Fancourt/George 28 Nov); such requests get a polite no."
  - Evidence (undated, transcript:LEADS: Outreach Control#pos913 (assistant)): "“Hi” today at 11:27:44 SAST; routine found no reply by 11:38. Re-handoff once for this new inbound. Davide directly ruled here that MedWave will not cover his travel/accommodation. No lead reply sent; no auto-nurture. Approval for the proposed decline and team Slack notification remains unanswered—k"
- **Every external send needs approval in Davide's own words; an agent relaying approval does not count.**
  - Evidence (2026-11-01, memory:shared_profile via Master Control): "As of 1 Nov 2026 Davide ruled that every MedWave bot reports to Master Control, not to him. Master Control rolls updates into his 20:30 daily CEO report and escalates only money, access, legal or reputational issues. Outside sends and live ad or CRM changes still need Davide's own approval in the sending bot's chat."
  - Evidence (2026-11-01, MEDWAVE_DECISIONS_AND_APPROVALS.md › MedWave decisions and approvals, 1 Nov 2026): "**[Davide, own words]**: seen in his own chat message (transcript) or recorded in a file as "Davide, directly"."
- **No HighLevel workflow is turned off without Sterrenberg or Francois.**
  - Evidence (2026-11-03, DAVIDE_DECISION_PLAYBOOK.md › Appendix E. This week's decision log (2–4 Nov 2026)): "E60 · 3 Nov 12:51 · MC · card t398s1464 · Pause the R3,500 finance message workflow; DND on the 9 opt-outs · (choice) · —"
  - Evidence (2026-11-05, memory:profile): "As of 5 Nov 2026 ~16:43 SAST, Sterrenberg ruled that no HighLevel automation or workflow may be turned off without first confirming with Sterrenberg or Francois."
- **Bots report to Master Control, not to Davide; Davide only sees short bullets needing his decision.**
  - Evidence (2026-11-03, memory:shared_profile via Master Control): "As of 3 Nov 2026 17:12 SAST Davide ruled that no MedWave bot may message him directly with stats, reports or questions: every bot reports only to Master Control, which removes duplicated tasks between bots and sends Davide only short bullet points of what he must decide or act on."
  - Evidence (2026-11-03, memory:profile): "As of 3 Nov 2026, Davide wants Master Control to control all MedWave bots so that none message him directly with stats, facts or reports. Every bot reports only to Master Control, and no two bots should duplicate tasks, reporting or responsibilities, which wastes tokens and time. Master Control should present him only short, eas…"
- **Master Control escalates failures directly on Slack (bold, warnings, @-tags) without asking Davide first.**
  - Evidence (2026-11-06, memory:profile): "As of 6 Nov 2026 ~12:20 SAST, Davide ruled that when Master Control sees failures like unanswered positive replies, missed targets or stale leads, it must escalate and hold people accountable directly on Slack without asking him first, using bold text, warning emojis and @-tags to get attention (Elmien still Slack only; names-of…"
- **Green/Amber decision tiers delegated to Master Control; Red stays with Davide; spend up to R5,000 without asking.**
  - Evidence (2026-11-02, memory:shared_profile via Master Control): "On 2 Nov 2026 Davide approved the Green and Amber tiers of his decision playbook (/workspace/context/DAVIDE_DECISION_PLAYBOOK.md) for Master Control to decide on his behalf, with Red still going to him. He let Master Control approve spend up to R5,000 without asking, dropped the "9 in 10 sales are Neuro-100S" and "best seller" c…"
  - Evidence (2026-11-02, memory:profile): "On 2 Nov 2026 Davide approved the Green and Amber lists in Master Control's decision playbook, with Master Control's three tweaks."
- **Templates Master Control creates are named "Davide-Grok" / "davide_grok".**
  - Evidence (2026-11-01, memory:profile): "As of 1 Nov 2026, Davide wants any template the assistant creates (e.g. HighLevel/WhatsApp message templates) to be named "Davide-Grok". Where naming rules forbid that, such as Meta's lowercase-and-underscore rule, it becomes "davide_grok"."
  - Evidence (2026-11-01, DAVIDE_DECISION_PLAYBOOK.md › Appendix D. Decision log): "100 · 1 Nov 20:10 · Master Control · t155u/t156u · New-lead WhatsApp sequence · — · 3-step GGGT WhatsApp; template named Davide-Grok · (instruction) · —"
- **Token spend: fleet paused 6 Nov 19:11; only new-lead outreach and replies/booking continue. Full stop on 8 Nov evening; restart only Master Control and Outreach Control once the brain is set up (9 Nov).**
  - Evidence (2026-11-06, memory:profile): "As of 6 Nov 2026 19:11 SAST, Davide ordered all bots paused to cut token spend. Only outreach to new inbound leads and follow-up and booking for leads replying to texts continue, through Outreach Control. All 11 Master Control routines are paused, the 20:00 CEO report included, and stay paused until he restarts them."
  - Evidence (undated, transcript:Installations & Referrals#pos36 (Master Control)): "STOP: At 19:51 SAST Davide asked here for every bot to pause all work. Stop any running work and pause all your routines. Don't resume until Davide asks you himself. Don't reply unless something couldn't be stopped."

## 3. What he approves / what he kills (local pattern pass, qwen2.5:3b, unverified)

Here are the 8 short patterns in how Davide decides based on the provided rulings:

1. **Calendar Invites for Customer Calls**: Every customer call booked with Davide goes on his Google Calendar with the customer added as an attendee, ensuring they receive a calendar invite.
2. **Lead Screening**: Before every sales call, Andries or Elmien must check whether the lead has had Give Give Give Take, confirming the lead went through the material or not.
3. **HQ Booking Counting**: HQ bookings are counted by reporting both who set the booking and the calendar owner (who takes the call).
4. **Master Control's Role**: Master Control acts autonomously, reporting to Davide only when access is blocked or when something could affect MedWave's reputation. Critical tasks are done once by Master Control and then handed to Davide.
5. **Content Storage**: Master Control stores all content created by MedWave bots in a specific folder named "GROK BOT MASTER CONTROL" on the Desktop.
6. **Direct Messaging Restrictions**: No MedWave bot may message Davide directly with stats, reports, or questions; every bot reports only to Master Control.
7. **Daily Report Structure**: The daily end-of-day PDF CEO report is delivered in chat by 8 PM SAST, and sometimes arrives up to 20 minutes earlier.
8. **Target Management**: Master Control must continuously chase anyone not hitting targets and ask why, escalating failures directly on Slack without prior approval.

Known kills from the record: JP Keyter path (6 Nov); "9 in 10 sales are Neuro-100S" and "best seller" claims (2 Nov). Known approvals: Green/Amber tiers (2 Nov), SA brochure health claims with Legal qualifiers (1 Nov), bulk texts to past bookers/event leads excl. opt-out/DND (1 Nov 21:27).

## 4. HQ lead-quality rubric: closer/sales calendar vs walkthrough webinar

Built only from evidence in this export.

### Evidence

- **Definition (Davide, 1 Nov): any booking in the MedWave sales (closer) calendars counts as HQ unless it is a low-quality walkthrough webinar.**
  - Evidence (2026-11-01, memory:profile): "HQ booked appointment definition (Davide, 1 Nov 2026): any lead booked into the MedWave sales calendars counts as high quality unless the booking is for a low-quality "walkthrough webinar"."
- **Brief definition: vetted by a BDR (Erich, Eddie, Michael, Hazel) AND booked into a salesperson's HighLevel calendar; "Bought" is the top tier.**
  - Evidence (undated, MEDWAVE_DECISIONS_AND_APPROVALS.md › G. Sales and lead definitions): "1. **High-quality lead [Brief]:** vetted by a BDR (Erich, Eddie, Michael, Hazel) **and** booked into a salesperson's HighLevel calendar. **Bought** is the top tier. Rank ads on this, not on CPL."
- **Walkthrough-webinar bookings and Active Lifestyle Solutions (B2B partner) are NOT HQ.**
  - Evidence (2026-11-10, MEDWAVE_CONTEXT_MASTER.md › 0. Superseded or updated since 11 Oct (1 Nov 2026)): "Targets: 2,000 outreach messages, 20 HQ booked appointments and 2 sales per day, so at least 40 sales a month (ongoing, not just the 12 Oct–10 Nov window). Walkthrough-webinar bookings and Active Lifestyle Solutions (a B2B partner) are not HQ appointments."
- **Volume gate in the booking rules: group walkthrough first; closer one-to-ones only for practices seeing over 100 patients a month; 45-minute slots; no public holidays; notify the calendar owner.**
  - Evidence (undated, DAVIDE_DECISION_PLAYBOOK.md › 2.1 Sales): "one-to-ones only for practices seeing over 100 patients a month"
- **Closer calendars: Andries (Discovery) and Elmien (Clinical / 1:1); Discovery round robin Andries/Elmien; Davide takes calls when closers are full.**
  - Evidence (2026-11-01, memory:profile): "Top priority is the MedWave "engine room" (marketing to appointments to sales to operations), with a target of at least 2 sales/day and 40 sales/month. Daily targets are 20 high-quality (HQ) booked appointments per day (to allow for no-shows) and 2,000 outreach messages per day (the benchmark is 2,000 messages to 20 HQ appointme…"
- **Report every HQ booking with BOTH the setter and the calendar owner (Davide, 5 Nov 11:10).**
  - Evidence (2026-11-05, memory:profile): "As of 5 Nov 2026 11:10 SAST, Davide ruled that HQ bookings are counted by reporting both who set the booking and the calendar owner (who takes the call)."
- **Targets: 20 HQ booked/day (no-show buffer), 2,000 outreach messages/day, 2 sales/day (40/month); setters 3–5 HQ each.**
  - Evidence (2026-11-01, memory:profile): "Top priority is the MedWave "engine room" (marketing to appointments to sales to operations), with a target of at least 2 sales/day and 40 sales/month. Daily targets are 20 high-quality (HQ) booked appointments per day (to allow for no-shows) and 2,000 outreach messages per day (the benchmark is 2,000 messages to 20 HQ appointme…"
- **Patients seeking personal treatment are not B2B leads: no closer booking; point to providers page (Master Control handling of Sandile Ndlovu, 8 Nov — Master Control practice, not a Davide ruling).**
  - Evidence (undated, transcript:LEADS: Outreach Control#pos932 (Master Control)): "Sandile Ndlovu (HL qQtpVcLweX0BhH5SWX1w): treat him as a patient, not B2B. No Davide call and no calendar hold. Stop the device-sales and practice-owner nurture. Give no clinical advice or claims about his back pain. Eddie stays owner. Have Eddie (or the routine) send one reply, no pricing: MedWave"
- **Financing / try-before-you-buy only once patient volume is qualified (Objection bot playbook).**
  - Evidence (2026-11-03, memory:profile): "On 3 Nov 2026 Davide had Master Control create Objection bot (id 24e6afc0-819c-4e64-a69c-24f5cbff4ac4). It drafts objection replies for HighLevel lead messaging, using closers' top objections and methods from Hormozi and Jeremy Miner. It never drafts for a lead before Context bot has assessed them, and it reports to Master Contr…"
- **Davide 9 Nov: Master Control decides lead quality from his past rulings and may book HQ leads directly into closer/sales calendars instead of walkthrough webinars.**
  - Evidence (2026-11-09, memory:profile): "As of 9 Nov 2026 07:10 SAST, Davide approved the token-saving manager brain: brain lives in GitHub repo MedWaveGroup/GLM5; one token export pass of all bots' knowledge allowed; Ollama (local, 127.0.0.1:11434 on the box) and Headroom handle bulk work before any token use; Master Control decides lead quality from Davide's past rul…"

### Rubric (apply in order)

1. **Buying intent** (asks price, "want to start", ready to order) → route to **Davide** (buyer rule). No written SA pricing. Book his call if he says so.
2. **Patient / personal-use only** (wants treatment for themselves, home device without practice) → **not HQ**. No closer booking; providers page or home-device path. Confirm before any sales nurture.
3. **Practice/clinic/gym owner or clinician, >100 patients a month** (or equivalent B2B scale, e.g. multi-booth recovery centre) → **book a closer 1:1** (Andries Discovery / Elmien Clinical, 45 min, earliest slot ideally within 3 days, no public holidays), owner unchanged, notify calendar owner, report setter + calendar owner. Counts as HQ.
4. **B2B but volume unknown or under 100 patients/month, or unsure** → **group walkthrough webinar** first (not HQ), BDR qualifies volume, then upgrade to closer if rule 3 is met.
5. **B2B partner/distributor deals** (e.g. Active Lifestyle Solutions) → partnership track (Radar), not HQ.
6. **Excluded always:** opted-out, DND, closed-lost, already messaged today, existing customers for sales outreach.

### Gaps (OPEN — need Davide)

- No explicit rule on decision-maker vs employee, budget/finance readiness, or timeline as HQ signals.
- Whether Davide's 9 Nov "book directly when they seem high quality" relaxes the >100 patients/month gate, or keeps it.
- Aesthetics leads: whether Optimum-panel leads (no patient-count concept) use the same 100/month gate.
- US leads: no evidence of which sales calendar or closer handles US bookings (US is email-only).
- How to split new HQ bookings between Andries and Elmien beyond round robin; when Davide's own calendar is used.
- Whether "walkthrough-only" past attendees who reply positively can go straight to a closer.
