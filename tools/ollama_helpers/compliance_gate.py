"""Pre-send compliance gate (advisory, box-side). Deterministic rules first; Ollama
only for an optional tone/claims second opinion. It never sends anything.

Input: JSON (file path or stdin) with keys:
  text, channel ("whatsapp"|"email"|"sms"), country ("ZA"|"US"), tags [..],
  segment ("doctor"|"physio"|"practitioner"|"patient"|...), campaign
  ("blast"|"reactivation"|"new_lead_retouch"|"reply"|"first_touch"),
  last_contact_at (ISO, optional), touches_today (int), emails_sent_today (int),
  prior_messages [..], booked (bool), dnd (bool)
Output: JSON {pass, blocks[], warns[], tags_to_add[], engine}
"""
from __future__ import annotations
import json, re, sys
from datetime import datetime, timezone, timedelta

from dedupe_wording import check as dedupe_check
from finance_quote import APPROVED_MONTHLY

SAST = timezone(timedelta(hours=2))
BOT_TAG = "davide-bot-outreach"
EMAIL_DAILY_CAP = 50
MAX_AUTO_TOUCHES_DAY = 3
APPROVED_AMOUNTS = set(APPROVED_MONTHLY.values())

RAND = re.compile(r"\bR\s?(\d{1,3}(?:[ ,]\d{3})+|\d+(?:\.\d+)?)\s*(k|m|mil|million)?\b", re.I)
USD = re.compile(r"(US\$|\$)\s?\d", re.I)
MONTHLY_WORDS = re.compile(r"(/\s?mo(nth)?\b|per month|a month|p/?m\b|monthly)", re.I)
PRICE_WORDS = re.compile(r"\b(price|pricing|cost|costs|rand|deposit|instal?ment|finance|financing|per month)\b", re.I)
BANNED = [
    (re.compile(r"\breply\s+stop\b", re.I), "use 'Reply 1 to opt out', never 'reply stop'"),
    (re.compile(r"\b(pay nothing|free trial|money[- ]back|guarantee[sd]?|cure[sd]?|ROI|earn(ings)?)\b", re.I),
     "claim/offer wording needs Davide (no cures, guarantees, earnings, ROI)"),
]
SIGNOFF = re.compile(r"(\n|^)\s*[-–—]?\s*(davide|dr\.?\s+\w+|medwave team|ceo)\W*$", re.I)


def _amounts(text: str) -> list[float]:
    out = []
    for num, suf in RAND.findall(text):
        v = float(num.replace(",", "").replace(" ", ""))
        if suf and suf.lower() == "k":
            v *= 1000
        elif suf:
            v *= 1_000_000
        out.append(v)
    return out


def gate(m: dict) -> dict:
    text = m.get("text", "")
    tags = [t.lower().strip() for t in m.get("tags", [])]
    channel = (m.get("channel") or "").lower()
    campaign = (m.get("campaign") or "").lower()
    blocks, warns = [], []

    # Hard stops
    if m.get("dnd") or any(t in ("dnd", "opt-out", "opt out", "no-contact", "no contact") for t in tags):
        blocks.append("DND / opt-out / no-contact")
    if m.get("booked") and campaign != "reply":
        blocks.append("lead already booked: never re-message from automation")
    if (m.get("country") or "").upper() == "US" and channel != "email":
        blocks.append("US lead: email only")
    if channel == "email" and int(m.get("emails_sent_today", 0)) >= EMAIL_DAILY_CAP:
        blocks.append(f"email cap {EMAIL_DAILY_CAP}/day reached: move volume to WhatsApp")
    if campaign != "reply" and int(m.get("touches_today", 0)) >= MAX_AUTO_TOUCHES_DAY:
        blocks.append("3 automated touches today already")

    # 24-hour rule (blasts + reactivation); 1-hour re-touch for new leads stays
    lc = m.get("last_contact_at")
    if lc and campaign in ("blast", "reactivation"):
        t = datetime.fromisoformat(lc.replace("Z", "+00:00"))
        if t.tzinfo is None:
            t = t.replace(tzinfo=SAST)
        if datetime.now(timezone.utc) - t < timedelta(hours=24):
            blocks.append("contacted in the last 24h: skip blast/reactivation")

    # Pricing rules
    amounts = _amounts(text) + ([1] if USD.search(text) else [])
    is_cpd = any("cpd" in t for t in tags)
    # Davide 12 Nov 2026 10:42 SAST: hold ALL pricing (finance amounts too) for
    # every CPD-tagged contact; "cpd - attended" is NOT an exemption.
    if amounts:
        if is_cpd:
            blocks.append("CPD-tagged contact: no pricing at all, finance amounts included")
        for v in _amounts(text):
            if v >= 10000:
                blocks.append(f"full price R{v:,.0f} in text: quote finance monthly amount only")
            elif not MONTHLY_WORDS.search(text):
                blocks.append(f"rand amount R{v:,.0f} without 'per month' wording")
            elif round(v) not in APPROVED_AMOUNTS:
                warns.append(f"R{v:,.0f}/month is not one of the approved 11%/60-month figures")
        if re.search(r"\b\d{1,2}(\.\d+)?\s?%|\binterest\b|\b\d{2}\s?months?\b|\bdeposit\b", text, re.I):
            blocks.append("lead-facing price text mentions rate, term or deposit: monthly amount only")
    elif is_cpd and PRICE_WORDS.search(text):
        warns.append("CPD lead and text talks about price/finance: check")

    # Wording rules
    for rx, why in BANNED:
        if rx.search(text):
            (blocks if "reply" in why else warns).append(why)
    if channel == "whatsapp":
        if SIGNOFF.search(text.strip()):
            blocks.append("WhatsApp text ends with a name/title sign-off")
        body = re.sub(r"reply 1 to (opt out|pause messages)\.?", "", text, flags=re.I).strip()
        if not body.rstrip().endswith("?"):
            warns.append("text should end on an open question")

    # No repeated wording to the same contact
    pri = m.get("prior_messages") or []
    engine = "deterministic"
    if pri:
        d = dedupe_check(text, pri, use_ollama=m.get("use_ollama", True))
        engine = d["engine"]
        if d["verdict"] == "repeat":
            blocks.append(f"repeats earlier wording (similarity {d['max_similarity']})")
        elif d["verdict"] == "review":
            warns.append(f"close to earlier wording (similarity {d['max_similarity']})")

    return {"pass": not blocks, "blocks": blocks, "warns": warns,
            "tags_to_add": [] if BOT_TAG in tags else [BOT_TAG], "engine": engine}


if __name__ == "__main__":
    raw = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    data = json.loads(raw)
    res = [gate(x) for x in data] if isinstance(data, list) else gate(data)
    print(json.dumps(res, indent=2))
