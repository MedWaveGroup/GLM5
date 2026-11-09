---
name: lead-triage-hq-booking
description: Use when a lead must be marked HQ or not, booked onto the closer sales calendar or the walkthrough webinar, and given an owner. Covers owned leads, unowned leads, buyers, SA pricing, Optimum versus Neuro, and US email only.
---

# Lead triage for HQ booking

## Rule

Local first, tokens last. This command is deterministic. It does not call Ollama and it does not spend paid tokens.

Standing rules, in order:

- Opted-out, DND, closed-lost, already messaged today, or an existing customer: do not contact.
- A patient or personal-use enquiry is not HQ. No closer booking.
- Owned leads stay with their owner. Unowned leads go to Erich.
- Buyers (price, "I want to start", ready to buy) go to Davide. No SA pricing before a call.
- Optimum for aesthetics. Neuro for medical.
- Over 100 patients a month: closer sales calendar, and that booking is HQ.
- Volume unknown or 100 or under: walkthrough webinar, not HQ.
- US outreach is email only. SMS and WhatsApp are blocked.

## Command

```bash
brain triage-lead '{"owner": null, "country": "ZA", "practice": true, "patients_per_month": 120, "setting": "medical"}'
```

Stdin works the same way:

```bash
echo '{"owner": "Hazel", "buying_intent": true, "country": "ZA", "message": "how much does it cost"}' | brain triage-lead
```

Read `hq`, `calendar` (`closer sales calendar`, `walkthrough webinar`, or `none`), and `owner`.
