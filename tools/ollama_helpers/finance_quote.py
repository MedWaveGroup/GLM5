"""Deterministic finance quote: 11% p.a., 60 months, on the excl.-VAT price, no balloon.
Leads are quoted the MONTHLY amount only, never the full price. No model call needed."""
from __future__ import annotations
import argparse, json

RATE, MONTHS = 0.11, 60
# Approved monthly figures (Davide, 12 Nov 2026). Full prices stay internal.
APPROVED_MONTHLY = {
    "Neuro Mobile + stand": 2174,
    "Optimum panel + stand": 3805,
    "Neuro 100-S panel + stand": 4131,
    "Recovery Booth": 5436,
    "Booth + Vibe package": 8153,
}


def monthly(principal: float, rate: float = RATE, months: int = MONTHS) -> float:
    r = rate / 12
    return principal * r / (1 - (1 + r) ** -months)


def lead_line(product: str) -> str:
    amt = APPROVED_MONTHLY[product]
    # Lead-facing: monthly amount only. No full price, no rate, no term, no deposit talk.
    return f"{product}: about R{amt:,} a month, excluding VAT"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--principal", type=float, help="internal check: excl.-VAT price")
    ap.add_argument("--lines", action="store_true", help="print approved lead-facing lines")
    a = ap.parse_args()
    if a.principal:
        print(json.dumps({"monthly": round(monthly(a.principal)), "rate": RATE, "months": MONTHS}))
    if a.lines or not a.principal:
        for p in APPROVED_MONTHLY:
            print(lead_line(p))
