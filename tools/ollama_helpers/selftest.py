"""Offline self-test for the helper scripts (no Ollama needed). Run: python3 selftest.py"""
from compliance_gate import gate
from dedupe_wording import similarity
from finance_quote import monthly
from privacy_scrub import scrub
from classify_reply import classify

FAKE_PHONE = "+27 82 " + "000 " + "0000"  # built at runtime so repo privacy scans stay clean


def t(name, cond):
    print(("PASS " if cond else "FAIL ") + name); return cond

ok = all([
    t("11%/60m on R100k = R2,174", round(monthly(100000)) == 2174),
    t("11%/60m on R190k = R4,131", round(monthly(190000)) == 4131),
    t("CPD no-event blocks price", not gate({"text": "About R4,131 a month, excluding VAT. Would that work?",
        "channel": "whatsapp", "tags": ["cpd opt-in"], "campaign": "reply"})["pass"]),
    t("CPD attended allows monthly", gate({"text": "About R4,131 a month, excluding VAT. Would that work?",
        "channel": "whatsapp", "tags": ["cpd opt-in", "cpd - attended"], "campaign": "reply"})["pass"]),
    t("full price blocked", not gate({"text": "It is R190 000 excl VAT. Does that fit?", "channel": "whatsapp", "campaign": "reply"})["pass"]),
    t("R100k blocked", not gate({"text": "Only R100k. Keen?", "channel": "whatsapp", "campaign": "reply"})["pass"]),
    t("US SMS blocked", not gate({"text": "Hi?", "channel": "sms", "country": "US"})["pass"]),
    t("email cap 50", not gate({"text": "Hi?", "channel": "email", "emails_sent_today": 50})["pass"]),
    t("reply stop blocked", not gate({"text": "Keen? Reply STOP to opt out", "channel": "whatsapp"})["pass"]),
    t("retouch exempt from 24h", gate({"text": "Did you get a chance to look?", "channel": "whatsapp",
        "campaign": "new_lead_retouch", "last_contact_at": "2099-01-01T00:00:00+02:00"})["pass"]),
    t("bot tag suggested", gate({"text": "Hi?", "channel": "whatsapp"})["tags_to_add"] == ["davide-bot-outreach"]),
    t("dedupe ignores names", similarity("Hi Anna, shall I send times?", "Hi Ben, shall I send times?") >= 0.8),
    t("scrub phone, keep date", scrub("2026-11-12 call " + FAKE_PHONE) == "2026-11-12 call [phone]"),
    t("STOP regex", classify("Please remove me", use_ollama=False)["label"] == "STOP"),
])
raise SystemExit(0 if ok else 1)
