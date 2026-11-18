---
title: "CPD-list doctors get no pricing until they attend an event"
tags: [medwave, brain, objections, standing-rules, rule]
source: "Davide Duranti, 12 Nov 2026 10:21 SAST, updated 10:42 SAST: no attendance exemption"
date: 2026-11-12
---

# CPD-list doctors get no pricing until they attend an event

Hold pricing for every CPD-tagged contact, with no exemptions. It is CPD, not CBD. They are identified by HighLevel tags containing "cpd" (case-insensitive) or by the list /workspace/team/outreach-control/cpd_contacts_2026-11-12.csv (1,206 contacts on 12 Nov). Send only an event invite or book a discovery call. The tag `cpd - attended` does not count as attending an online event and does not lift the hold, until Davide names a real attendance signal. Do not add CPD contacts to the opt-out suppression list just because they have a CPD tag; this is a hold rule, not an opt-out.

## Trigger phrases

- a contact whose tags contain cpd
- CPD list, CPD opt-in, CPD attended, CPD not attended
- doctor on a CPD list asks the price, the monthly amount, or for finance figures

## Rule

- If any HighLevel tag contains "cpd" (case-insensitive), or the contact ID is on `/workspace/team/outreach-control/cpd_contacts_2026-11-12.csv`, treat the lead as being on a CPD list.
- Hold all pricing for every such contact, with no exemptions. No price line, no monthly figures, no finance amounts, no deposits, no packages, no "starts at".
- SUPERSEDED 12 Nov 2026 10:42 SAST: the tag `cpd - attended` does not count as attending a MedWave online event and does not lift this hold. `cpd - not attended` also stays on the hold. Until Davide names a real attendance signal, no CPD contact gets pricing.
- Only an event invite or a 1:1 discovery call (Meet link, 45 minutes at :00 or :30). Never a walkthrough in place of that discovery call for practitioners.
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
- Any monthly amount to a contact who has the tag `cpd - attended` — that tag is not an exemption

## Source and date

- Davide Duranti, 12 Nov 2026 10:21 SAST, updated 10:42 SAST: hold every CPD contact, no attendance exemption

Related: [[guardrails]] · [[monthly-prices-only]] · [[patient-price]] · [[standing-rules]] · [[davide-decisions]] · [[Start here]]
