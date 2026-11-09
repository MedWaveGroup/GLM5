"""HQ lead triage. Deterministic. No model call."""

from __future__ import annotations

import re


CLOSER = "closer sales calendar"
WALKTHROUGH = "walkthrough webinar"
NONE = "none"


def _text(payload: dict) -> str:
    parts = []
    for key in ("message", "text", "notes", "intent", "role", "type", "setting", "context", "name"):
        value = payload.get(key)
        if value:
            parts.append(str(value))
    return " ".join(parts)


def _country(payload: dict) -> str:
    raw = str(payload.get("country") or payload.get("region") or "").strip().lower()
    if raw in {"us", "usa", "u.s.", "u.s.a.", "united states", "america"}:
        return "US"
    if raw in {"za", "sa", "rsa", "south africa"}:
        return "ZA"
    return raw.upper()


def _flag(payload: dict, *keys: str) -> bool:
    for key in keys:
        value = payload.get(key)
        if value is True or (isinstance(value, str) and value.lower() in {"true", "yes", "1"}):
            return True
    return False


def _buying(payload: dict, text: str) -> bool:
    if _flag(payload, "buying_intent", "buyer"):
        return True
    intent = str(payload.get("intent") or "").lower()
    if intent in {"buy", "buying", "buyer", "ready"}:
        return True
    return bool(
        re.search(
            r"how much|what(?:'s| is) the price|\bpricing\b|want to start|ready to (buy|order)|i want to buy",
            text,
            re.I,
        )
    )


def _patient(payload: dict, text: str) -> bool:
    if _flag(payload, "patient_use", "personal_use", "patient"):
        return True
    role = str(payload.get("role") or payload.get("type") or "").lower()
    if role in {"patient", "personal", "consumer", "b2c"}:
        return True
    return bool(re.search(r"\b(for myself|personal use|home device|my back|patient)\b", text, re.I))


def _practice(payload: dict, text: str) -> bool:
    if _flag(payload, "practice", "b2b"):
        return True
    role = str(payload.get("role") or payload.get("type") or "").lower()
    return bool(re.search(r"practice|clinic|clinician|doctor|gym|owner|b2b|spa", role + " " + text, re.I))


def _partner(payload: dict, text: str) -> bool:
    if _flag(payload, "partner", "distributor"):
        return True
    return "active lifestyle" in text.lower()


def _setting(payload: dict, text: str) -> str | None:
    raw = str(payload.get("setting") or "").strip().lower()
    if raw in {"aesthetics", "aesthetic", "spa", "skin", "beauty"}:
        return "aesthetics"
    if raw in {"medical", "clinic", "physio", "doctor"}:
        return "medical"
    blob = f"{payload.get('context') or ''} {text}".lower()
    aesthetics = bool(re.search(r"aesthetic|spa|skin clinic|beauty", blob))
    medical = bool(re.search(r"\bmedical\b|physio|hospital", blob))
    if aesthetics and not medical:
        return "aesthetics"
    if medical and not aesthetics:
        return "medical"
    if aesthetics:
        return "aesthetics"
    return None


def _patients(payload: dict) -> int | None:
    for key in ("patients_per_month", "patients", "volume"):
        value = payload.get(key)
        if value is None or value == "":
            continue
        if isinstance(value, bool):
            continue
        try:
            return int(value)
        except (TypeError, ValueError):
            match = re.search(r"\d+", str(value))
            if match:
                return int(match.group(0))
    return None


def _owner_in(payload: dict) -> str | None:
    owner = payload.get("owner")
    if owner is None:
        return None
    text = str(owner).strip()
    if text.lower() in {"", "none", "null", "unassigned", "unowned"}:
        return None
    return text


def _excluded(payload: dict) -> str | None:
    if _flag(payload, "opted_out", "optedout"):
        return "opted out"
    if _flag(payload, "dnd"):
        return "DND"
    if _flag(payload, "closed_lost"):
        return "closed-lost"
    if _flag(payload, "existing_customer"):
        return "existing customer"
    if _flag(payload, "messaged_today"):
        return "already messaged today"
    return None


def triage_lead(payload: dict) -> dict:
    """Apply the HQ rubric and the standing owner rules.

    Order: exclusions, patient use, partner track, buying intent, then the
    volume gate. Owned leads keep their owner unless the buyer rule sends the
    action to Davide. Unowned leads go to Erich. US is email only. No SA price
    is ever written into the result.
    """
    text = _text(payload)
    reasons: list[str] = []
    country = _country(payload)
    record_owner = _owner_in(payload)
    patients = _patients(payload)
    setting = _setting(payload, text)
    product = None
    if setting == "aesthetics":
        product = "Optimum"
        reasons.append("Optimum panel only in aesthetics settings.")
    elif setting == "medical":
        product = "Neuro"
        reasons.append("Neuro panel in medical settings.")

    us = country == "US"
    channel = "email" if us else ("whatsapp" if country in {"ZA", ""} else "unspecified")
    requested = str(payload.get("channel_requested") or "").lower()
    channel_blocked = bool(us and requested in {"sms", "whatsapp", "wa", "imessage", "text"})
    if us:
        reasons.append("US outreach is email only.")
        channel = "email"
    if channel_blocked:
        reasons.append(f"Requested channel {requested} is blocked for a US lead.")

    no_sa_pricing = country != "US"
    if no_sa_pricing:
        reasons.append("No SA pricing before a sales call.")

    excluded = _excluded(payload)
    owner = record_owner or "Erich"
    if record_owner:
        reasons.append(f"Owned lead stays with {record_owner}.")
    else:
        reasons.append("No owner on the lead, so it goes to Erich.")

    if excluded:
        reasons.append(f"Excluded ({excluded}). Do not contact and do not book.")
        return _result(
            hq=False,
            calendar=NONE,
            owner=owner,
            product=product,
            channel=channel,
            channel_blocked=channel_blocked,
            no_sa_pricing=no_sa_pricing,
            reasons=reasons,
            rule="excluded",
            do_not_contact=True,
            record_owner=record_owner,
        )

    patient = _patient(payload, text)
    practice = _practice(payload, text)
    if patient and not practice:
        reasons.append("Personal-use or patient lead is not HQ. No closer booking. Point to the providers page.")
        if _buying(payload, text):
            owner = "Davide"
            reasons.append("Buying intent still routes to Davide, with no written price.")
        return _result(
            hq=False,
            calendar=NONE,
            owner=owner,
            product=product,
            channel=channel,
            channel_blocked=channel_blocked,
            no_sa_pricing=no_sa_pricing,
            reasons=reasons,
            rule="patient-not-hq",
            do_not_contact=False,
            record_owner=record_owner,
        )

    if _partner(payload, text):
        reasons.append("B2B partner or distributor track (Radar), not an HQ booking.")
        return _result(
            hq=False,
            calendar=NONE,
            owner=owner,
            product=product,
            channel=channel,
            channel_blocked=channel_blocked,
            no_sa_pricing=no_sa_pricing,
            reasons=reasons,
            rule="partner-not-hq",
            do_not_contact=False,
            record_owner=record_owner,
        )

    buyer = _buying(payload, text)
    if buyer:
        owner = "Davide"
        reasons.append("Buyer rule: route to Davide, not back to a setter or closer.")
        if record_owner:
            reasons.append(
                f"HighLevel record owner {record_owner} is not reassigned; the person who acts is Davide."
            )
        if not practice:
            reasons.append("Clarify practice versus personal use before booking a calendar.")
            return _result(
                hq=False,
                calendar=NONE,
                owner=owner,
                product=product,
                channel=channel,
                channel_blocked=channel_blocked,
                no_sa_pricing=no_sa_pricing,
                reasons=reasons,
                rule="buyer-clarify",
                do_not_contact=False,
                record_owner=record_owner,
            )

    volume_hq = patients is not None and patients > 100
    if practice or buyer:
        if volume_hq:
            reasons.append(
                "Practice seeing over 100 patients a month: book a closer 1:1 (45 min). This counts as HQ."
            )
            calendar = CLOSER
            hq = True
            rule = "closer-over-100"
        elif patients is not None and patients <= 100:
            reasons.append(
                "Volume is 100 or under: group walkthrough webinar first. Not HQ until volume clears the gate."
            )
            calendar = WALKTHROUGH
            hq = False
            rule = "walkthrough-under-100"
        else:
            reasons.append("B2B volume unknown: group walkthrough webinar first, then upgrade if the gate is met. Not HQ.")
            calendar = WALKTHROUGH
            hq = False
            rule = "walkthrough-volume-unknown"
        if buyer and volume_hq:
            reasons.append("Davide takes the buyer. Calendar is still the closer sales calendar.")
        elif buyer and not volume_hq:
            reasons.append("Buyer goes to Davide. Volume is not HQ, so the default booking is the walkthrough unless he takes the call.")
        return _result(
            hq=hq,
            calendar=calendar,
            owner=owner,
            product=product,
            channel=channel,
            channel_blocked=channel_blocked,
            no_sa_pricing=no_sa_pricing,
            reasons=reasons,
            rule=rule,
            do_not_contact=False,
            record_owner=record_owner,
        )

    reasons.append("Not enough to call this a practice lead. Do not book a closer. Confirm who they are.")
    return _result(
        hq=False,
        calendar=NONE,
        owner=owner,
        product=product,
        channel=channel,
        channel_blocked=channel_blocked,
        no_sa_pricing=no_sa_pricing,
        reasons=reasons,
        rule="unknown",
        do_not_contact=False,
        record_owner=record_owner,
    )


def _result(**kwargs) -> dict:
    record_owner = kwargs.pop("record_owner")
    result = {
        "hq": kwargs["hq"],
        "calendar": kwargs["calendar"],
        "owner": kwargs["owner"],
        "record_owner": record_owner,
        "product": kwargs["product"],
        "channel": kwargs["channel"],
        "channel_blocked": kwargs["channel_blocked"],
        "no_sa_pricing": kwargs["no_sa_pricing"],
        "do_not_contact": kwargs["do_not_contact"],
        "rule": kwargs["rule"],
        "reasons": kwargs["reasons"],
        "route": "rule",
        "escalate_paid": False,
        "escalate_human": False,
        "reason": None,
    }
    return result
