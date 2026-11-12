---
title: "Objection guardrails"
tags: [medwave, brain, objections, rule]
source: "Objection bot playbook v1.4 (3-4 Nov 2026); Davide Duranti rules 11-12 Nov 2026"
date: 2026-11-12
---

# Objection guardrails

These hard rules apply to every objection reply. Pull this note together with the matching objection card. Do not load the full playbook into a paid model.

## Rule

- Honour opt-outs, the suppression list and DND. Never work around DND. Never message anyone on the suppression list.
- Doctors on any CPD list (HighLevel tags containing "cpd", case-insensitive; it is CPD not CBD) get no pricing of any kind — no price line, no monthly figures, no finance amounts — until they have attended a MedWave online event. Only an event invite or a discovery call. See [[cpd-no-pricing]]. Attendance is confirmed by the tag `cpd - attended`.
- Never quote full equipment prices to leads. SUPERSEDED 12 Nov 2026 10:21 SAST: R100,000 / R190,000 / R100k / R190k and any other list price. For everyone who is allowed a price, use only the monthly amounts in [[monthly-prices-only]], excluding VAT, with no deposit. Do not mention interest rate, term length or other finance terms in lead-facing wording.
- The no-money-down line is only for confirmed healthcare providers, never for patients, and never mentions 90 days or terms: "We have no-money-down options for practitioners like yourself. Would you like to hear about our flexible options?"
- The patient price line is only for confirmed patients, never for practitioners, and never for a CPD-hold doctor. The 11 Nov full-price line is SUPERSEDED. PENDING Davide's wording confirmation, the replacement is: "Thanks for your interest. Our home-use Neuro-100S Mobile works out to about R2,174 a month and our flagship medical Neuro-100S about R4,131 a month, both excluding VAT, with no deposit. Does that fit within your budget? If so, I'd be happy to set up a quick call." See [[patient-price]].
- If a confirmed patient says the price is too expensive, send www.medwavegroup.com/providers, then move them to no-contact and set DND.
- A cancellation is never a price decline. Do not send the patient price line, the providers link, or set DND just because someone cancelled a slot.
- "Already a MedWave or provider in my area" is an objection to handle, not a reason to close, set DND, or move to no-contact. The two practitioner / B2B replies are approved (12 Nov 2026, 06:25 SAST). For a patient lead with this objection, notify their owner only; do not send a reply.
- Before any blast or reactivation send (the daily quiet-lead batch counts as reactivation): skip anyone who received any MedWave message (bot, BDR or closer, any channel) in the last 24 hours, checked against HighLevel conversation history. Reactivation also keeps the stricter 48-hour skip. Do not apply the 24-hour skip to the 1-hour re-touch of brand-new unreplied leads. See [[send-windows]].
- Brand-new unreplied leads keep the 1-hour re-touch: at most 3 automated touches a day, each adding something new, stopping on reply, booking, opt-out or owner pickup.
- Never send a contact the same or near-identical wording twice. Compare against their past outbound HighLevel messages. This applies to every send, including re-touches.
- Sequence membership (N1, B1–B5) is shown only by the HighLevel sequence tag. Exact names: `n1`, `n1 - b5`, `b1`, `b1 - b5`, `b2`, `b3`, `b4`, `b5`. Pause if contacted in the last 24 hours. Book immediately on reply.
- US leads get email only. Elmien is Slack only. External sends need Davide's own words.
- One question per message. Helpful tone, SA/UK English. We sell a system, not a box.
- In lead copy say "red light (PBM)", never "red light therapy". Do not invent statistics.
- Weekday playbook sends may add: "– [Name], MedWave Group. Reply 1 to pause messages."

## Do not say

- Any full equipment list price (R100,000, R190,000, R100k, R190k or similar) — SUPERSEDED 12 Nov 2026 10:21 SAST
- Monthly or finance amounts to a CPD-list doctor who has not attended a MedWave online event
- Interest rate, 60 months, instalments, payment plan, or other terms in lead copy
- 90 days or any payment terms, including when using the no-money-down line
- The patient price line to a doctor, physio, clinic, gym owner or other practitioner
- The no-money-down line to a patient
- Legal or contract wording, or medical efficacy claims that are not approved

## Source and date

- Objection bot playbook v1.4, 3-4 Nov 2026, `/workspace/team/objection-bot/playbook_v1.4.md`
- Patient price line (full prices): SUPERSEDED. Original: Davide Duranti, 11 Nov 2026
- Monthly-only amounts, CPD no pricing, 24-hour blast/reactivation skip, no repeated wording, 1-hour re-touch, N1/B1–B5 sequence tags: Davide Duranti, 12 Nov 2026 10:21–10:25 SAST, relayed by Master Control
- Patient too expensive: Davide Duranti, 11 Nov 2026 (share www.medwavegroup.com/providers, then no-contact and DND)
- No-money-down line: Davide, healthcare providers only, used in reactivation 11 Nov 2026
- Cancellation is not a price decline: Outreach Control / Master Control, 12 Nov 2026 (Chanelle Kemp incident)
- Already a provider nearby: Davide Duranti, 12 Nov 2026, 06:21 SAST

Related: [[objections]] · [[already-a-provider-nearby]] · [[patient-price]] · [[cpd-no-pricing]] · [[monthly-prices-only]] · [[send-windows]] · [[cancellation-is-not-a-price-decline]] · [[standing-rules]] · [[Start here]]
