"""Inbound reply classifier: deterministic opt-out / auto-reply / booked regex first,
then local Ollama for the label. Escalates (escalate_paid) only when Ollama is down
or returns an unknown label. Read-only: no HighLevel calls, no sends.

  echo '{"text":"How much is it?"}' | python3 classify_reply.py
  python3 classify_reply.py --text "Not interested thanks"
"""
from __future__ import annotations
import argparse, json, re, sys

LABELS = ("positive", "question", "price_question", "buyer", "will_call_back", "negative",
          "STOP", "patient-consumer", "auto-reply", "area_objection")
STOP_RE = re.compile(r"^\s*(please\s+)?stop\W*$|\bunsubscribe\b|\bopt[\s-]?out\b|\bremove\s+me\b|"
                     r"\bnot\s+interested\b|\bdon'?t\s+(text|message|contact|call|email)\b|"
                     r"^\s*1\s*$|\bverwyder\b", re.I)
AUTO_RE = re.compile(r"\b(out of (the )?office|auto[- ]?reply|automatic reply|on leave until|"
                     r"thank you for contacting|we will get back to you)\b", re.I)
PRICE_RE = re.compile(r"\b(how much|price|pricing|cost|quote|rate|finance|monthly)\b", re.I)
AREA_RE = re.compile(r"\b(already (a|one|have)|another provider|provider (near|in my)|in my (area|town))\b", re.I)

SYSTEM = ("You label WhatsApp/email replies to a medical-equipment company (MedWave). "
          "Labels: " + ", ".join(LABELS) + ". 'buyer' = wants to buy/asks for invoice or contract. "
          "'patient-consumer' = a patient wanting treatment for themselves, not a practice. "
          "'area_objection' = says a provider already exists in their area (never a reason to close). "
          "Reply only JSON {\"label\": ..., \"confidence\": 0-1, \"why\": short}.")


def classify(text: str, use_ollama: bool = True) -> dict:
    t = text.strip()
    if STOP_RE.search(t):
        return {"label": "STOP", "engine": "regex", "action": "DND + suppress"}
    if AUTO_RE.search(t):
        return {"label": "auto-reply", "engine": "regex", "action": "ignore; no re-touch count"}
    hint = "price_question" if PRICE_RE.search(t) else ("area_objection" if AREA_RE.search(t) else None)
    if use_ollama:
        try:
            import ollama_local
            from privacy_scrub import scrub
            out = ollama_local.generate(f"Reply: {scrub(t)[:800]}", system=SYSTEM, json_mode=True,
                                        step="classify_reply", num_predict=60)
            d = json.loads(out) if out else None
            if d and d.get("label") in LABELS:
                d["engine"] = "ollama"
                if hint and d["label"] in ("question", "positive"):
                    d["label"], d["why"] = hint, f"{d.get('why','')} (regex hint)"
                return d
        except Exception:
            pass
    if hint:
        return {"label": hint, "engine": "regex"}
    return {"label": None, "engine": "none", "escalate_paid": True,
            "why": "Ollama unavailable or unsure"}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--text")
    ap.add_argument("--no-ollama", action="store_true")
    a = ap.parse_args()
    txt = a.text if a.text is not None else json.loads(sys.stdin.read())["text"]
    print(json.dumps(classify(txt, not a.no_ollama)))
