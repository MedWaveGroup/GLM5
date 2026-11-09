"""Deterministic MedWave rules. First match wins. No model, no tokens."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Rule:
    id: str
    title: str
    patterns: tuple[str, ...]
    ruling: str
    citation: str
    human: bool = False
    paid: bool = False


@dataclass(frozen=True)
class Gap:
    id: str
    title: str
    patterns: tuple[str, ...]
    note: str


# Operational rules, most specific first. Citations point at the decision model.
RULES: tuple[Rule, ...] = (
    Rule(
        id="spend-cap",
        title="Green/Amber delegated; Red and spend above R5,000 stay with Davide",
        patterns=(
            r"R\s?(?:[6-9][,\s]?\d{3}|[1-9]\d[,\s]?\d{3,})",
            r"\b(?:spend|budget|approve)\b.{0,40}\b(?:above|over|more than)\b.{0,20}R\s?5[, ]?000",
            r"\bR\s?5[, ]?000\b",
            r"\bred tier\b",
        ),
        ruling=(
            "Spend up to R5,000 on a Green or Amber item can be approved by Master Control "
            "and reported afterwards. Anything above R5,000, or a Red item, goes to Davide."
        ),
        citation="decision-model §2, Davide 2 Nov 2026 (Green/Amber approved, Red stays with him).",
        human=True,
    ),
    Rule(
        id="no-sa-pricing-before-call",
        title="No SA pricing in writing before a sales call",
        patterns=(
            r"\bpric",
            r"how much",
            r"\bcost\b",
            r"\bquote\b",
        ),
        ruling="Do not send a South African price. Offer a call. Price questions go to Davide.",
        citation="decision-model §2, Davide rule, evidenced 5 Nov 2026 (no SA pricing before a sales call).",
    ),
    Rule(
        id="buyer-rule",
        title="Buyers go to Davide",
        patterns=(
            r"buying intent",
            r"\bbuyer\b",
            r"want to start",
            r"ready to (buy|order)",
            r"i want to buy",
        ),
        ruling="Route buying intent to Davide himself, not back to a setter or closer.",
        citation="decision-model §2, buyer rule (Davide handles leads with buying intent).",
    ),
    Rule(
        id="external-send-needs-davide",
        title="External sends need Davide's own words",
        patterns=(
            r"external send",
            r"own words",
            r"approve the (send|message|text|email)",
            r"send (the )?(whatsapp|email|sms|brochure) .{0,30}(without|before) approval",
        ),
        ruling="Do not send anything external until Davide approves it in his own words. A bot relaying approval does not count.",
        citation="decision-model §2, 1 Nov 2026 (outside sends need Davide's own approval).",
        human=True,
    ),
    Rule(
        id="no-workflow-off",
        title="No HighLevel workflow off without Sterrenberg or Francois",
        patterns=(
            r"workflow",
            r"turn\w* off",
            r"disabl\w+ (an? )?(automation|workflow)",
            r"pause\w* (an? )?(automation|workflow|nurture)",
        ),
        ruling="Do not turn off a HighLevel workflow or automation unless Sterrenberg or Francois has confirmed it.",
        citation="decision-model §2, Sterrenberg 5 Nov 2026.",
    ),
    Rule(
        id="elmien-slack-only",
        title="Elmien is Slack only",
        patterns=(r"\belmien\b",),
        ruling="Contact Elmien on Slack only. Do not WhatsApp, SMS, or email her from the bots.",
        citation="decision-model §2, standing rule as of 5 Nov 2026.",
    ),
    Rule(
        id="us-email-only",
        title="US outreach is email only",
        patterns=(
            r"\bUS\b.{0,40}(sms|whatsapp|text|imessage)",
            r"(sms|whatsapp|text).{0,40}\bUS\b",
            r"\bunited states\b",
            r"\bus lead\b",
            r"\bus outreach\b",
        ),
        ruling="US outreach is email only. Do not send SMS or WhatsApp. There is no evidence of SMS consent on the US form.",
        citation="decision-model §2, Anthony Polenski 5 Nov 2026.",
    ),
    Rule(
        id="owned-leads-stay",
        title="Owned leads stay with their owner",
        patterns=(
            r"already (has|have) an owner",
            r"\bowned leads?\b",
            r"do not reassign",
            r"never reassign",
            r"keep (their|the) owner",
        ),
        ruling="A lead that already has an owner stays with that owner. Do not reassign them.",
        citation="decision-model §2, Davide 6 Nov 2026.",
    ),
    Rule(
        id="unowned-leads-erich",
        title="Unowned leads go to Erich",
        patterns=(
            r"unowned",
            r"no (clear )?owner",
            r"without an owner",
            r"unassigned",
        ),
        ruling="Assign the lead to Erich now. Leads with no clear owner in HighLevel go to Erich.",
        citation="decision-model §2, Davide 6 Nov 2026.",
    ),
    Rule(
        id="optimum-neuro",
        title="Optimum for aesthetics, Neuro for medical",
        patterns=(
            r"\boptimum\b",
            r"\bneuro\b",
            r"\baesthetic",
            r"which (panel|product|device)",
        ),
        ruling="Offer the Optimum panel only in aesthetics settings. Offer Neuro (Neuro100S) in medical settings.",
        citation="decision-model §2, Davide 7 Nov 2026.",
    ),
    Rule(
        id="no-travel",
        title="MedWave does not pay lead travel or accommodation",
        patterns=(
            r"\b(travel|accommodation|flights?|hotel)\b",
        ),
        ruling="MedWave does not pay a lead's travel or accommodation. Decline politely.",
        citation="decision-model §2, Davide 6 Nov 2026 (Fancourt/George).",
    ),
    Rule(
        id="bots-report-to-mc",
        title="Bots report to Master Control",
        patterns=(
            r"report to davide",
            r"message davide",
            r"who do bots report",
            r"bots report",
        ),
        ruling="Bots report to Master Control, not to Davide. He only sees short bullets that need his decision.",
        citation="decision-model §2, Davide 3 Nov 2026.",
    ),
    Rule(
        id="escalate-on-slack",
        title="Escalate failures on Slack without asking first",
        patterns=(
            r"missed target",
            r"unanswered",
            r"stale lead",
            r"hold .{0,20}accountable",
        ),
        ruling="Master Control escalates failures on Slack (bold, warnings, @-tags) without asking Davide first. Elmien stays Slack only.",
        citation="decision-model §2, Davide 6 Nov 2026 ~12:20 SAST.",
    ),
    Rule(
        id="opt-out",
        title="Opted-out contacts stay, and are never messaged",
        patterns=(r"opt[- ]?out", r"\bdnd\b", r"\bstop\b reply"),
        ruling="Keep opted-out contacts in HighLevel with DND on and the Opted out tag. Never delete them and never message them.",
        citation="Davide 1 Nov 2026. SA WhatsApp opt-out wording is Reply 1. US SMS is Reply STOP.",
    ),
    Rule(
        id="hq-definition",
        title="HQ is a closer-calendar booking, not a walkthrough",
        patterns=(
            r"\bHQ\b",
            r"high[- ]quality",
            r"walkthrough",
            r"closer calendar",
            r"100 patients",
        ),
        ruling=(
            "A booking on a MedWave sales (closer) calendar is HQ unless it is a walkthrough webinar. "
            "Closer one-to-ones are for practices seeing over 100 patients a month. "
            "Under that, or if volume is unknown, book the group walkthrough first. That is not HQ."
        ),
        citation="decision-model §4, Davide 1 Nov 2026 definition, plus the volume gate in the playbook.",
    ),
    Rule(
        id="templates",
        title='Templates are named Davide-Grok',
        patterns=(r"template name", r"davide-grok", r"davide_grok"),
        ruling='Name templates "Davide-Grok". Where the channel forces lowercase, use "davide_grok".',
        citation="decision-model §2, Davide 1 Nov 2026.",
    ),
    Rule(
        id="targets",
        title="Daily engine-room targets",
        patterns=(
            r"\btargets?\b",
            r"2,?000",
            r"20 hq",
            r"how many (bookings|sales|messages|whatsapps)",
        ),
        ruling="Daily targets are 20 HQ bookings, 2,000 outreach messages, and 2 sales (40 a month).",
        citation="decision-model §4 and the engine-room priority, Davide 1 Nov 2026.",
    ),
)


GAPS: tuple[Gap, ...] = (
    Gap(
        id="decision-maker",
        title="Decision-maker versus employee is not an HQ signal",
        patterns=(
            r"decision[- ]maker",
            r"\bemployee\b.{0,30}\bHQ\b",
            r"\bbudget\b.{0,40}\bHQ\b",
            r"\btimeline\b.{0,30}\bHQ\b",
        ),
        note="No explicit rule on decision-maker versus employee, budget, or timeline as HQ signals.",
    ),
    Gap(
        id="nine-nov-gate",
        title="9 Nov direct-booking versus the 100-patient gate",
        patterns=(
            r"9 nov.{0,80}(100|gate|relax|directly)",
            r"book directly.{0,40}(high quality|hq|100)",
            r"relax\w* the .{0,20}100",
        ),
        note="OPEN whether Davide's 9 Nov 'book directly when they seem high quality' relaxes the over-100-patients gate.",
    ),
    Gap(
        id="aesthetics-gate",
        title="Aesthetics leads and the 100-patient gate",
        patterns=(
            r"aesthetic\w*.{0,40}(100|patient|gate)",
            r"(100|patient|gate).{0,40}aesthetic",
        ),
        note="OPEN whether Optimum (aesthetics) leads use the same over-100-patients gate. There is no patient-count concept on a spa.",
    ),
    Gap(
        id="us-calendar",
        title="Which calendar handles US bookings",
        patterns=(
            r"\bUS\b.{0,50}(which|what).{0,20}(calendar|closer)",
            r"(which|what).{0,30}(calendar|closer).{0,40}\bUS\b",
            r"\bUS\b.{0,30}(andries|elmien).{0,30}(calendar|book)",
        ),
        note="OPEN which sales calendar or closer handles US bookings. US outreach is email only.",
    ),
    Gap(
        id="closer-split",
        title="Andries versus Elmien beyond round robin",
        patterns=(
            r"split.{0,30}(andries|elmien)",
            r"beyond round robin",
            r"when (is|does) davide'?s? (own )?calendar",
        ),
        note="OPEN how to split new HQ bookings between Andries and Elmien beyond round robin, and when Davide's own calendar is used.",
    ),
    Gap(
        id="walkthrough-upgrade",
        title="Walkthrough attendees going straight to a closer",
        patterns=(
            r"walkthrough.{0,40}(straight|directly).{0,20}closer",
            r"past attendees?.{0,30}closer",
        ),
        note="OPEN whether walkthrough-only past attendees who reply positively can go straight to a closer.",
    ),
)


def first_rule(text: str) -> Rule | None:
    for rule in RULES:
        if any(re.search(pattern, text, re.I) for pattern in rule.patterns):
            return rule
    return None


def first_gap(text: str) -> Gap | None:
    for gap in GAPS:
        if any(re.search(pattern, text, re.I) for pattern in gap.patterns):
            return gap
    return None
