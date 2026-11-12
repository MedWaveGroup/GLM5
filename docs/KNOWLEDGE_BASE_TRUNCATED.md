# MedWave bot operation: truncated knowledge base

**Version:** 12 Nov 2026, 10:45 SAST · **Owner:** Master Control · **For:** Davide Duranti and the GLM5 repo (MedWaveGroup/GLM5)

This is the short version of how the MedWave bot fleet runs today. Where this file and an older note disagree, this file wins, because it includes the rulings from 11 and 12 Nov. The full history is in `sources/decision-model.md` and the decision playbook. There are no secrets, tokens, webhook values, phone numbers or customer personal data in this file.

*How it was built:* the contact-rule, booking, lifecycle, routing and objection sections were drafted first by local Ollama (`qwen2.5:3b`, 127.0.0.1:11434, `tools/ollama_helpers/summarise.py`). Master Control then checked and edited them against the source files and today's rulings. The raw Ollama drafts are in `docs/ollama_drafts/`.

---

## 1. Core rules (read these first)

1. **Davide's own words or his card answers are the only approval.** A bot, a note or a task brief is not approval.
2. **Ollama first.** Every task starts with rules and lookups, then local Ollama. A paid model is used only when Ollama can't do the job (see section 8).
3. **Check the brain first.** Look in `/workspace/brain-export` (decision-model.md and notes/) for past rulings before spending tokens.
4. **Only finance prices.** Leads hear the monthly finance amount only, never the full price.
5. **CPD doctors get no price before an event.** A doctor with a CPD tag hears no pricing until they have attended one of our online events.
6. **One voice to Davide.** Every bot reports to Master Control. Master Control sends Davide short bullets, and only for what needs his decision or reply.
7. **Nothing stops the engine room.** The engine room is marketing → appointments → sales → operations. The daily targets are 2,000 WhatsApps, 20 HQ bookings and 2 sales (40 a month).

## 2. Bot roster and reporting lines

| Who | Role | Reports to |
|---|---|---|
| **Master Control (MC)** | Runs the fleet, holds context, assigns work, writes Davide's bullets | Davide |
| **LEADS: Outreach Control (OC)** | Lead operations: WhatsApp batches, reactivation, replies, bookings, the reply-watcher handoffs | MC (Davide talks to OC directly about leads) |
| LEADS: Outreach Bot | Finds and engages B2B leads by segment | OC |
| LEADS: Objection bot | Writes replies to objections from the playbook | OC |
| LEADS: Context bot | Builds each lead's context and interaction record | OC |
| LEADS: Wording Lab | Writes and tests message wordings | OC |
| Sales Desk | Books calls on closer calendars, with notice | OC / MC |
| Communication bot | Watches the MedWave Slack and routes requests | MC |
| Messaging Performance | Daily messaging metrics report | MC |
| Deposits & Finance, Installations & Referrals, Reporting, QA, Legal, Content, Meta Ads and others | Their own areas | MC (never Davide directly) |
| **Mac reply watcher** (launchd, on Davide's Mac) | Polls HighLevel replies every 2 min, classifies with Ollama, sends fixed-template standard replies, hands non-standard replies to the paid live-reply routine | OC |
| **Box new-lead watcher** | Picks up website-form leads, sends the after-hours CEO holding line and a one-hour nudge, and queues daytime leads for OC | OC |

**Human team.** Davide is CEO. Francois is CRO and manages the setters. The setters (BDRs) are Erich, Michael, Hazel and Eddie. Sterrenberg owns automations, BI, blasts and reactivation. Elmien and Andries are the closers. Anthony runs the US. Ian is COO.

## 3. Lead lifecycle

1. **Intake.** Leads come in from website forms, ads, CPD and event lists, reactivation lists and inbound replies. US leads are kept apart, and they get email only.
2. **Screening, deterministic.** Leads with DND, opt-out, "not interested", suppression, an existing booking, an internal or test flag, or membership of the MedWave Community WhatsApp group (no bulk to that group) are dropped.
3. **Classification, Ollama.** Replies are sorted into positive, question, price question, buyer, will call back, negative, STOP, patient/consumer, auto-reply or area objection.
4. **First touches give value (GGGT).** Touches 1 to 3 are gives (brochure, recording, info link). The ask comes from touch 4 onwards. The approved reactivation templates are the exception, and Davide has accepted them.
5. **Qualification.** A lead that wants to move forward in any way, even just booking a call, counts as **HQ**. Doctors and physios (checked against the HighLevel contact card) go to a **1:1 discovery call, never a walkthrough**.
6. **Booking.** See section 6. Bot bookings are Davide's bookings, and Davide is made the HighLevel owner.
7. **Pre-call brief.** Davide gets a WhatsApp brief 10 minutes before each call on his calendar. It goes to Davide only.
8. **After booking.** Booked leads are never re-messaged by automation. HQ bookings are reported with both the setter and the calendar owner.
9. **Closed or lost.** A patient who says the price is too much gets the providers link, then no-contact and DND. **"There's already a provider in my area" is never a reason to close, DND or no-contact a lead.** It gets one of the approved restaurant or capacity replies.

## 4. Pricing rules

- **Never quote a full price to a lead.** That rules out R100,000, R190,000, R100k, R190k and every other list price. Quote the monthly amount only. Internally it is worked out at 11% over 60 months on the excl.-VAT price, with no balloon. **Lead-facing wording never mentions the interest rate, the term or a deposit.**

| Product (lead-facing name) | Say to the lead |
|---|---|
| Neuro Mobile + stand | **about R2,174 a month, excl. VAT** |
| Optimum panel + stand | **about R3,805 a month, excl. VAT** |
| Neuro 100-S panel + stand | **about R4,131 a month, excl. VAT** |
| Recovery Booth | **about R5,436 a month, excl. VAT** |
| Booth + Vibe package | **about R8,153 a month, excl. VAT** |

- **CPD gate.** A contact with any `cpd …` tag (for example `cpd opt-in`, `cpd - web invite`, `cpd - intro - msg1/2`, `cpd - not attended`, `cpd - davide sent`) gets **no pricing or finance figures at all** until they carry `cpd - attended`, meaning they have been to an online event.
- **Practitioners** get the soft line: *"We have no-money-down options for practitioners like yourself. Would you like to hear about our flexible options?"*
- **Patients** get the price, then the budget question ("Does that fit within your budget?"). If yes, book a call. If no, send the providers link, then no-contact and DND. *Open point: the 11 Nov patient line used the full R100k/R190k prices. That line is withdrawn. The replacement quotes the Neuro Mobile and Neuro 100-S monthly amounts, then asks the budget question. It is **pending Davide's wording confirmation**, so hold patient price sends until he confirms.*
- United Capital's own quotes work out to roughly 17–20% (except Booth and Vibe). Don't use their rental figures with leads.
- **US** prices are USD and email only. No medical-device wording goes in US copy.
- `tools/ollama_helpers/finance_quote.py` holds the approved monthly figures and the formula. Use it rather than doing the maths by hand.

## 5. Contact rules

- **Opt-out, DND and suppression always win.** Check the suppression list before every send. "Not interested" means no more automated messages, permanently. The opt-out line is "Reply 1 to opt out", never "reply stop".
- **24-hour rule (12 Nov).** Blasts and reactivation skip anyone contacted in the last 24 hours. The current WhatsApp batches use a stricter 48-hour window.
- **One-hour re-touch.** Brand-new leads still get one re-touch after one hour if they haven't replied. The 24-hour rule does not change this.
- **No repeated wording.** No contact gets the same or near-same wording twice. The dedupe check is in `tools/ollama_helpers/dedupe_wording.py`.
- **At most 3 automated touches a day.** A contact with 7 or more automated messages in 7 days goes into a 7-day cool-off.
- **Email is capped at 50 a day** across the bot runs ("don't destroy my email server"). All volume goes on WhatsApp.
- **Tag `davide-bot-outreach`** on every contact the bots message, so Sterrenberg can filter them out of his own blasts.
- **Send window (SA).** The main bulk run is 09:00–10:59 SAST, Mon–Fri. Back-up slots are 12:00 and 18:00. Avoid 08:00 and 17:00.
- **Text style.** WhatsApp texts carry no name or title sign-off and end on an open question. Email may carry the CEO sign-off.
- **Channels.** US leads get email only (no SMS without proof of consent). Elmien gets her follow-up nudges on **Slack only**. Other staff can be nudged on Slack or WhatsApp.
- **Wallet.** On "insufficient funds", resend once after 2–5 minutes, then warn Sterrenberg urgently. Stop on a Meta limit.

## 6. Booking rules

- Calls start only on **:00 or :30**, with **45 minutes** kept free. **No double-booking.**
- Elmien and Andries bookings are **at least 30 minutes**. Every booking carries a **Google Meet link** for the lead.
- Doctors and physios get a 1:1 discovery call. Elmien's and Davide's calendars come first, then Andries's, picking whoever has the most open slots.
- Davide's calendar is used only if the lead is not already booked with Andries or Elmien and the HighLevel notes show no notes or outreach from either of them.
- Walkthrough-webinar bookings are **not HQ**.

## 7. Lead routing

- **Buyers go to Davide.**
- HQ leads go to Erich's pipeline. Other leads go to BDRs in performance order: Erich, then Michael, then Hazel and Eddie, spread between them. A BDR who is behind or has many unread messages gets no new leads until they catch up.
- An existing owner keeps the lead. If Erich has spoken to the lead, it stays Erich's. If Erich is assigned but hasn't booked or spoken to the lead, it is open and goes to Davide.
- A lead a bot books counts as Davide's, and Davide becomes the HighLevel owner.

## 8. Escalation

| Trigger | Goes to |
|---|---|
| Lead-specific wording, an objection not in the library, Ollama down, low confidence, or two failed local drafts | Paid model (MC or OC live-reply routine) |
| Buyer, deposit or contract intent | Davide |
| Red items, spend above R5,000, a new type of external send, open policy gaps | Davide (approval card) |
| HighLevel workflow changes | **Never by a bot.** Sterrenberg or Francois only |
| Reply needs a human owner | Owner nudge (Elmien on Slack only) |
| Wallet "insufficient funds" after one resend | Sterrenberg, urgently |

## 9. Security rules (binding)

- Never print or report HIGHLEVEL_PIT_TOKEN, LEAD_WATCHER_WEBHOOK_URL, LEAD_WATCHER_WEBHOOK_KEY or any webhook URL or header value. Never print the MedX pull token in `~/.config/medwave/ledger.env`.
- Ollama runs on **loopback only** (127.0.0.1:11434). **No tunnels.** Headroom compression stays on the machine, and tunnels are forbidden.
- Never push `brain-export/raw/`, which is not redacted. Never ingest `context/confidential/`.
- Never type credentials, and never put passwords or codes in chat.
- Don't unload lead-coordinator (PID 7017) without Davide's say-so.
- Only one reply watcher runs at a time, and it runs on the Mac. Don't start the box copy.
- Run `tools/ollama_helpers/privacy_scrub.py --check` over every file before it goes into the repo.
