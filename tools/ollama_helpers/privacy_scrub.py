"""Redact emails, phone numbers and secret-shaped strings before text leaves a script
(or goes into an Ollama prompt / a repo file). Deterministic, no model."""
from __future__ import annotations
import re, sys

PATTERNS = [
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "[email]"),
    (re.compile(r"\b\d{8,15}@s\.whatsapp\.net\b"), "[jid]"),
    (re.compile(r"\b(pit|sk|pk|rk|ghp|gho|xox[abp])[-_][A-Za-z0-9_-]{12,}\b", re.I), "[secret]"),
    (re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,}\b"), "[jwt]"),
    (re.compile(r"(?i)(bearer\s+)[A-Za-z0-9._-]{16,}"), r"\1[secret]"),
    (re.compile(r"(?i)https?://[^\s)]*(webhook|hooks?\.)[^\s)]*"), "[webhook-url]"),
]


PHONE = re.compile(r"(?<![\w/:.-])\+?\d[\d\s().-]{7,}\d(?![\w/:-])")
DATE_LIKE = re.compile(r"^\d{4}-\d{2}-\d{2}$|^\d{1,2}[ -]\d{1,2}[ -]\d{2,4}$")


def _phone(m: re.Match) -> str:
    s = m.group(0)
    digits = re.sub(r"\D", "", s)
    if len(digits) < 9 or DATE_LIKE.match(s.strip()) or re.fullmatch(r"\d{1,3}(,\d{3})+", s):
        return s
    return "[phone]"


def scrub(text: str) -> str:
    for rx, rep in PATTERNS:
        text = rx.sub(rep, text)
    return PHONE.sub(_phone, text)


def findings(text: str) -> list[str]:
    f = [rep for rx, rep in PATTERNS if any(m.group(0) != rep for m in rx.finditer(text))]
    if PHONE.sub(_phone, text).count("[phone]") > text.count("[phone]"):
        f.append("[phone]")
    return f


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    data = open(args[0]).read() if args else sys.stdin.read()
    if "--check" in sys.argv:
        f = findings(data)
        print("CLEAN" if not f else "FOUND: " + ", ".join(sorted(set(f))))
        sys.exit(1 if f else 0)
    sys.stdout.write(scrub(data))
