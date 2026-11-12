---
title: "CPD-list doctors get no pricing until they attend an event"
tags: [medwave, brain, objections, standing-rules, rule]
source: "Davide Duranti, 12 Nov 2026 10:21 SAST, relayed by Master Control"
date: 2026-11-12
---

# CPD-list doctors get no pricing until they attend an event

Doctors on any CPD list get no pricing of any kind until they have attended a MedWave online event. It is CPD, not CBD. They are identified only by HighLevel tags containing "cpd" (case-insensitive). Until attendance is confirmed, send only an event invite or book a discovery call. Do not add CPD contacts to the opt-out suppression list just because they have a CPD tag; this is a hold rule, not an opt-out.

## Trigger phrases

- a contact whose tags contain cpd
- CPD list, CPD opt-in, CPD attended, CPD not attended
- doctor on a CPD list asks the price, the monthly amount, or for finance figures

## Rule

- If any HighLevel tag contains "cpd" (case-insensitive), treat the lead as being on a CPD list.
- Hold all pricing until a MedWave online event has been attended. No price line, no monthly figures, no finance amounts, no deposits, no packages, no "starts at".
- Attendance is confirmed by the tag `cpd - attended`. The tag `cpd - not attended` means they have not attended: still no pricing.
- Until attendance is confirmed, only an event invite or a 1:1 discovery call (Meet link, 45 minutes at :00 or :30). Never a walkthrough in place of that discovery call for practitioners.
- After confirmed attendance, they are no longer under this hold. Then the monthly-only rule in [[monthly-prices-only]] applies. Still never quote full equipment prices.
- Do not mention interest rate, term length or other finance terms in lead-facing wording.

## Exact CPD tag names found in HighLevel (SA location, 12 Nov 2026)

- `cpd opt-in`
- `cpd - attended`
- `cpd - not attended`
- `cpd - 10 nov`
- `cpd - web invite`
- `cpd - davide sent`
- `cpd - intro - msg1`
- `cpd - intro - msg2`
- `cpd - intro - msg3`

Any future tag containing "cpd" also triggers the hold, even if it is not in this list.

## Do not say

- Any price, monthly amount, finance amount, deposit, package total, or "starts at" figure
- The patient price line, even the monthly version
- The no-money-down line together with figures

## Source and date

- Davide Duranti, 12 Nov 2026 10:21 SAST, relayed by Master Control

Related: [[guardrails]] · [[monthly-prices-only]] · [[patient-price]] · [[standing-rules]] · [[davide-decisions]] · [[Start here]]
