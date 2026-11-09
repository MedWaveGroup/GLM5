"""Pick the simplest owner and the next step for a task."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Assignment:
    id: str
    patterns: tuple[str, ...]
    owner: str
    next_step: str
    rule: str
    human: bool = False


# First match wins, so keep narrow rules above broad ones.
ASSIGNMENTS: tuple[Assignment, ...] = (
    Assignment(
        id="external-approval",
        patterns=(r"external send", r"his own words", r"approve (the )?(send|message|whatsapp)"),
        owner="Davide",
        next_step="Wait for approval in Davide's own words before anything is sent outside the company.",
        rule="Every external send needs Davide's own approval.",
        human=True,
    ),
    Assignment(
        id="buyer",
        patterns=(r"buying intent", r"\bbuyer\b", r"how much", r"\bprice\b", r"ready to buy"),
        owner="Davide",
        next_step="Route the lead to Davide. Do not send an SA price. Offer a call.",
        rule="Buyers go to Davide. No SA pricing before a call.",
    ),
    Assignment(
        id="spend",
        patterns=(r"R\s?(?:[6-9],\d{3}|[1-9]\d,\d{3}|\d{5,})",),
        owner="Davide",
        next_step="This is above the R5,000 Green/Amber cap. Ask Davide.",
        rule="Spend above R5,000 stays with Davide.",
        human=True,
    ),
    Assignment(
        id="workflow",
        patterns=(r"workflow", r"automation", r"turn off", r"disable"),
        owner="Sterrenberg",
        next_step="Confirm with Sterrenberg or Francois before any HighLevel workflow is turned off.",
        rule="No HighLevel workflow is turned off without Sterrenberg or Francois.",
    ),
    Assignment(
        id="unowned",
        patterns=(r"unowned", r"no owner", r"no clear owner", r"unassigned"),
        owner="Erich",
        next_step="Assign the lead to Erich in HighLevel now.",
        rule="Unowned leads go to Erich.",
    ),
    Assignment(
        id="elmien",
        patterns=(r"\belmien\b",),
        owner="Elmien",
        next_step="Contact Elmien on Slack only.",
        rule="Elmien is Slack only.",
    ),
    Assignment(
        id="install",
        patterns=(r"install",),
        owner="Janae",
        next_step="Janae owns installations. Hand her the booking and the site.",
        rule="Janae keeps installations.",
    ),
    Assignment(
        id="referral",
        patterns=(r"referral",),
        owner="Karin Duranti",
        next_step="Karin owns referrals. Log it with her.",
        rule="Referrals are owned by Karin Duranti.",
    ),
    Assignment(
        id="stock",
        patterns=(r"\bstock\b", r"fulfil", r"fulfill"),
        owner="Ian",
        next_step="Ian owns stock and fulfilment.",
        rule="Ian keeps stock and fulfilment.",
    ),
    Assignment(
        id="finance",
        patterns=(r"deposit", r"agreement", r"\bfinance\b"),
        owner="Ian",
        next_step="Email Ian or Francois directly with the blocker. No draft is required.",
        rule="Stuck agreements and missing deposits go to Ian or Francois.",
    ),
    Assignment(
        id="event",
        patterns=(r"\bevent\b", r"webinar"),
        owner="Francois",
        next_step="Francois owns in-person events and webinars.",
        rule="Francois sets up events and webinars.",
    ),
    Assignment(
        id="setters",
        patterns=(r"\bsetter\b", r"\bbdr\b", r"text blast", r"outreach volume"),
        owner="Francois",
        next_step="Francois manages the setters. Ask him for the gap against 3 to 5 HQ each.",
        rule="BDRs report to Francois.",
    ),
    Assignment(
        id="clinical",
        patterns=(r"clinical",),
        owner="Elmien",
        next_step="Elmien takes the clinical 1:1. Slack only. Check Give Give Give Take before the call.",
        rule="Elmien is the clinical closer.",
    ),
    Assignment(
        id="closer",
        patterns=(r"\bcloser\b", r"discovery call", r"\bgggt\b", r"sales call"),
        owner="Andries",
        next_step="Andries (Discovery) or Elmien (Clinical, Slack only) checks Give Give Give Take before the call.",
        rule="Closers Andries and Elmien own GGGT before and after every call.",
    ),
    Assignment(
        id="legal",
        patterns=(r"\blegal\b", r"sahpra", r"\bfda\b", r"\bnrcs\b"),
        owner="Ian",
        next_step="Ian owns the chase. Do not go back to the previous consultant.",
        rule="NRCS and FDA chase sits with Ian.",
    ),
    Assignment(
        id="report",
        patterns=(r"\breport\b", r"\bkpi\b", r"dashboard", r"eod\b"),
        owner="Master Control",
        next_step="Roll it into Master Control. Davide only gets a short decision bullet.",
        rule="Bots report to Master Control, not to Davide.",
    ),
)


def assign_rule(task: str) -> Assignment | None:
    for item in ASSIGNMENTS:
        if any(re.search(pattern, task, re.I) for pattern in item.patterns):
            return item
    return None


def assignment_dict(item: Assignment) -> dict:
    return {
        "owner": item.owner,
        "next_step": item.next_step,
        "rule": item.rule,
        "rule_id": item.id,
        "route": "rule",
        "escalate_paid": False,
        "escalate_human": item.human,
        "reason": "Needs Davide." if item.human else None,
    }
