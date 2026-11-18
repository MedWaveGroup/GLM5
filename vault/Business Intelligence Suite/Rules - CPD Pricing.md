---
title: "Rules - CPD Pricing"
tags: [medwave, bi-suite, cpd]
bi_type: rules
updated: 2026-11-12
refreshed_sast: "2026-11-12 11:14"
source: "refresh_bi_suite.py (Google Sheets + read-only HighLevel export)"
privacy: "no emails or phone numbers"
binding: true
set_by: "Davide Duranti, 12 Nov 2026"
---
# Rules - CPD Pricing and Contact

Suite: [[Business Intelligence Suite/Home|Home]] · [[Business Intelligence Suite/CPD Attendees Dashboard|CPD dashboard]] · [[Business Intelligence Suite/Pipeline & Conversion|Pipeline]] · [[Business Intelligence Suite/Follow-up Priorities|Follow-ups]] · [[Business Intelligence Suite/Rules - CPD Pricing|Rules]] · [[Business Intelligence Suite/Data Dictionary|Data dictionary]] · [[Business Intelligence Suite/How to Refresh|Refresh]]

Binding. Set by Davide Duranti on 12 Nov 2026 (SAST). Only Davide can change them.

## Pricing

1. **Every CPD-tagged doctor gets no pricing at all** — not monthly figures, not ranges, not "from" prices — until Davide changes this rule. Any HighLevel tag containing `cpd` triggers the hold.
2. **`cpd - attended` does not unlock pricing.** Attending an online event is not enough on its own; the hold stays for every CPD-tagged doctor (Davide, 12 Nov, card answer).
3. Doctors on the CPD lists Davide shared are treated the same even if HighLevel has no CPD tag yet (Davide: "make sure that outreach control does not send pricing to any doctors on our CPD lists"). In this suite every master row has `pricing_hold = YES`.
4. **Full prices are never quoted to anyone** (no R100k / R190k / R350k lines). Where pricing is allowed for non-CPD leads, only the monthly finance amounts are used, without stating the rate or term.
5. CPD doctors can still get event invites and discovery-call bookings.

## Barefoot list — never contact

6. **Doctors who appear only on the Barefoot Bytes spreadsheet must never be contacted** (no WhatsApp, no SMS, no email, no bot reply, no re-touch). Davide, 12 Nov 2026 14:34 SAST: "All these are coming from the Barefoot Bytes spreadsheet. You cannot text message them. You can just save them in the vault inside of the business intelligence suite." They are data only. The never-contact list is `/workspace/team/outreach-control/barefoot_no_contact_2026-11-12.csv` (copied to the Mac watcher as `~/medwave/lead-watcher/barefoot_no_contact.csv`). Do not add a HighLevel DND or any HighLevel tag for them.
7. The 73 doctors who are also on a webinar attendee or did-not-attend list **may** be reached. If they have no HighLevel owner, assign them to Erich. (Davide, 12 Nov 2026 14:34 SAST.)

## Contact

- At most 3 automated touches a day; 24-hour gap for blasts and reactivation; no repeated wording.
- Leads in an N1 or B1–B5 sequence: pause bot sends if messaged in the last 24 hours; a reply to a sequence message is hot — pick up at once and book a 1:1 discovery call. No one-hour re-touch for leads in a sequence.
- Booked leads are never re-messaged by bots. DND and opt-out are always respected.
- Email is capped at 50 a day; volume goes on WhatsApp. US leads get email only.
- Never edit HighLevel workflows without Sterrenberg or Francois.

Related: [[standing-rules]] · [[objections]] · [[Business Intelligence Suite/Home|BI Home]]
