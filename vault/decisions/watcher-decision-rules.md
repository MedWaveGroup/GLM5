---
title: Watcher decision rules
tags: [medwave, brain, decisions, watcher, index]
source: "Davide Duranti rulings, 12–13 Nov 2026"
date: 2026-11-13
---

# Watcher decision rules

Plain if/then rules the lead watcher applies directly, without asking Davide. One card per rule. Later dated rulings win when two rules overlap.

## If / then

1. **Ownership precedence** (13 Nov 2026 10:15 SAST) — [[ownership-precedence]]
   IF Davide, or a bot acting for him, is talking to the same person as any other rep, THEN move the lead to Davide without asking. Hierarchy: Davide, then Elmien, then Andries. Apply this across duplicate contacts. This supersedes "owned leads stay with their owner" in that case.

2. **Bot pickup owner** (13 Nov 2026 09:57 SAST) — [[bot-pickup-owner]]
   IF a bot picks up a conversation with a lead, THEN set the HighLevel owner to Davide (user id `kh4Y6pIfJEbjF27zgLuB`).

3. **Book confirmed times fast** (13 Nov 2026 09:57 SAST) — [[book-confirmed-times]]
   IF a provider replies on any channel with a clear day and time (for example a provider emailed asking for Monday 11:30), THEN book it ASAP on Davide's calendar `8ZAQgVCBzVM1NhCfrRWh` (start at :00 or :30, keep 45 minutes free) and email the date, time (SAST) and Google Meet link in the same thread. IF the time is ambiguous, THEN ask one short clarifying question offering 2 slots.

4. **Channel coverage** — [[channel-coverage]]
   IF watching for provider replies, THEN check HighLevel email (TYPE_EMAIL, Mailgun domain go.medwavemailer.com) as well as Gmail, HighLevel WhatsApp and Davide's personal WhatsApp. Provider email replies land in HighLevel, not Gmail.

5. **Andries's calendar** (12 Nov 2026 20:29 SAST) — [[andries-calendar-blackout]]
   IF booking Andries between 09:00 and 10:00 SAST, THEN do not. Use Elmien first, then Davide. A provider-confirmed time still goes on Davide's calendar.

6. **Post-reply follow-ups** (12 Nov 2026 17:01 SAST) — [[post-reply-follow-ups]]
   IF a lead replied and then went quiet, THEN touch them again even if they are in an N1, B1–B5 or other sequence, within the caps, and push toward a booking.

7. **Sequence replies** (12 Nov 2026 10:24 SAST) — [[sequence-replies]]
   IF a sequence lead replies, THEN pick up the conversation immediately and book them.

8. **Short separate texts** (13 Nov 2026 10:21 SAST) — [[short-separate-texts]]
   IF sending a message to a lead, THEN send short, succinct lines, each as its own separate text one after the next (for example 3 short texts). Never send one long message, so it feels more human.

## Never override

These hard stops always apply. No watcher rule above lets you skip them.

- Barefoot list doctors are never contacted (no WhatsApp, SMS or email, any send kind).
- Honour DND, opt-outs and the suppression list. Never work around DND.
- Booked leads get no more outreach.
- CPD-tagged doctors get no pricing at all, including the tag `cpd - attended`.
- Never quote full equipment prices; monthly amounts only, excl. VAT, no deposit, and only when pricing is allowed.
- Finance, legal and contract questions go to Davide.
- Email outreach is capped at 50 a day.
- No contact ever gets the same or near-identical wording twice.

Related: [[ownership-precedence]] · [[bot-pickup-owner]] · [[book-confirmed-times]] · [[channel-coverage]] · [[andries-calendar-blackout]] · [[post-reply-follow-ups]] · [[sequence-replies]] · [[short-separate-texts]] · [[standing-rules]] · [[objections]] · [[guardrails]]

## Rule 9: Booking titles (Davide, 13 Nov 2026 10:28 SAST, relayed by Master Control)
IF a bot books an appointment for Davide THEN title it exactly "Discovery call with Davide — {practitioner name}". Never put "Master Control" or any bot name in the title.

## Rule 10: Practitioner cash price line (Davide, 13 Nov 2026 12:06 SAST, card answer)
The one exception to "never quote full equipment prices". IF a non-CPD practitioner (healthcare provider, never a CPD-tagged doctor, never a patient) asks the price THEN the watcher may send this line word for word, split into short separate texts: "The cash price for our entry system is R100,000, and it goes up to R350,000, excluding VAT. Most practices pay this off in 2-3 months." CPD-tagged doctors (including 'cpd - attended') still get no pricing at all.

## Rule 11: Saturday blackouts (Davide, t1247u in Master Control's chat, 13 Nov 2026 14:00 SAST)
IF a booking or slot offer falls on any Saturday THEN never use Andries's calendar. IF it falls on Saturday 14 Nov 2026 THEN never use Davide's calendar either (he is away that weekend). Offer weekday times instead.

## Rule 12: 15-minute human-first window (Davide t367u, 13 Nov 2026 15:09 SAST)
Weekday team hours 07:00-17:00 SAST: IF a lead replies (including to a HighLevel workflow/sequence message) THEN wait 15 minutes from the inbound. Bots reply or book ONLY if no human outbound has been sent in that conversation since the inbound. If a person answered within 15 minutes, leave it alone.
After hours 17:00-07:00 SAST (Davide t368u, 15:10): reply within 1 minute of every inbound, no wait. Normal replies and booking all night, no out-of-office switch at 20:00 (Davide card answer 16:24).
Weekends (Saturday and Sunday, Davide card answer 13 Nov 16:24): reply within 1 minute all day, no 15-minute wait.
After 20:00 (Davide t371u, 16:24): first reply in a conversation introduces the bot as 'the out of office AI team, here to help you schedule a win-win call with our team' (short separate texts), then normal replies and booking.

## Rule 13: Roseanne's pipeline is off-limits (Davide t1262u in MC's chat, 13 Nov 2026 16:33 SAST)
IF a contact has an opportunity in Roseanne's HighLevel pipeline THEN bots do nothing with it: no outreach, replies, bookings, tags or owner changes. Contact ids: /workspace/team/reengage/roseanne_pipeline_contacts.txt.

## Rule 14: Asked where we got their details = DND (Davide t1271u in MC's chat, 14 Nov 2026 16:40 SAST)
IF a lead asks where MedWave got their details (how did you get my number/email, where did you get my details) THEN set DND in HighLevel, tag dnd-where-details, send nothing further, ever. First case: Lubovya Tambwe (vFLKoicegnHF8UvQmyxq). Contact ids: /workspace/team/reengage/dnd_where_details_contacts.txt; send_filters.py hard-blocks the ids and the tag (reason where_details_dnd_never_contact).
