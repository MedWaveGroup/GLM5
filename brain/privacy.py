"""Redact emails, phone numbers, and secrets. Slack and HighLevel IDs stay."""

from __future__ import annotations

import re

# Full addresses, then bare mailbox locals such as "erich@" or "janae@."
# A local is an @ that is not followed by a domain. Sentence periods count.
_FULL_EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
_LOCAL_EMAIL = re.compile(
    r"(?<![\w@])[A-Za-z0-9._%+-]{2,}@(?=\s|[,;)\]\"']|\.(?:\s|$)|$)"
)

# International numbers, including a trailing period. Dates, Slack timestamps,
# and HighLevel ids do not match.
_PHONE = re.compile(
    r"(?<![\w.])(?:\+\d{1,3}(?:[\s.-]\d{2,4}){2,3}|\+\d{10,15})(?!\d)"
)
_SA_PHONE = re.compile(r"\b0[1-8]\d{8}\b")

_SECRETS = [
    re.compile(r"sk_(live|test)_[A-Za-z0-9]+"),
    re.compile(r"xox[abposr]-[A-Za-z0-9-]+"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]+"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{8,}"),
    re.compile(r"(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*\S+"),
    re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----"),
]

# What a repo scan should treat as a leak. Bare locals are included.
SCAN_EMAIL = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    r"|(?<![\w@])[A-Za-z0-9._%+-]{2,}@(?=\s|[,;)\]\"']|\.(?:\s|$)|$)"
)
SCAN_PHONE = _PHONE
SCAN_SA_PHONE = _SA_PHONE
SCAN_SECRETS = _SECRETS


def redact(text: str) -> str:
    """Replace emails, phones, and secret-shaped strings. Idempotent on [email]/[phone]."""
    if not text:
        return text
    for rx in _SECRETS:
        text = rx.sub("[secret-redacted]", text)
    text = _FULL_EMAIL.sub("[email]", text)
    text = _LOCAL_EMAIL.sub("[email]", text)
    text = _PHONE.sub("[phone]", text)
    text = _SA_PHONE.sub("[phone]", text)
    return text


def leaks(text: str) -> list[str]:
    """Return human-readable leak labels found in text. Empty means clean."""
    found: list[str] = []
    if SCAN_EMAIL.search(text):
        found.append("email")
    if SCAN_PHONE.search(text) or SCAN_SA_PHONE.search(text):
        found.append("phone")
    for rx in SCAN_SECRETS:
        if rx.search(text):
            found.append("secret")
            break
    return found
