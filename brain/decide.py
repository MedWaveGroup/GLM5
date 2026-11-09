"""Apply decision-model.md. Rule first, then a local model, then the paid flag."""

from __future__ import annotations

import re

from brain.ollama_client import OllamaPool
from brain.retrieve import VaultIndex
from brain.router import base_result, escalate, run_local
from brain.rules import first_gap, first_rule
from brain.paths import vault_dir


_AMOUNT = re.compile(r"R\s?(\d[\d ,]{2,}\d)")


def _amount_over_cap(text: str) -> bool:
    for match in _AMOUNT.findall(text):
        digits = re.sub(r"[^\d]", "", match)
        if digits and int(digits) > 5000:
            return True
    return False


def _facts(question: str, limit: int = 4) -> list[dict]:
    vault = vault_dir()
    if not vault.exists():
        return []
    try:
        index = VaultIndex.load(vault)
    except Exception:
        return []
    return [hit.as_dict() for hit in index.search(question, k=limit)]


def decide(
    situation: str,
    pool: OllamaPool | None = None,
    model: str | None = None,
) -> dict:
    """Return the ruling, the rule it cites, and whether a paid model or a human is needed."""
    rule = first_rule(situation)
    gap = first_gap(situation)
    facts = _facts(situation)

    # An open gap with no operational rule is Davide's, not a paid model's.
    if gap and rule is None:
        return base_result(
            route="rule",
            answer=f"OPEN. {gap.note}",
            rule=gap.title,
            rule_id=gap.id,
            escalate_paid=False,
            escalate_human=True,
            reason=gap.note,
            facts=facts,
        )

    if rule is not None:
        human = rule.human or (rule.id == "spend-cap" and _amount_over_cap(situation))
        # Mentioning the R5,000 cap is not itself an escalation.
        if rule.id == "spend-cap" and not _amount_over_cap(situation):
            human = False
        answer = rule.ruling
        reason = None
        if gap and gap.id != rule.id:
            answer += f" Open gap still stands: {gap.note}"
            if gap.id in {"us-calendar", "aesthetics-gate", "nine-nov-gate", "closer-split", "walkthrough-upgrade"}:
                human = True
                reason = gap.note
        if human and reason is None:
            reason = "This one stays with Davide."
        return base_result(
            route="rule",
            answer=answer,
            rule=rule.title,
            rule_id=rule.id,
            escalate_paid=False,
            escalate_human=human,
            reason=reason,
            facts=facts,
        )

    pool = pool or OllamaPool()
    prompt = (
        "You are Master Control for MedWave. Decide the situation using only the facts. "
        "If the facts do not contain a rule, say you do not know. "
        "Four short lines: the ruling, the rule you cite, whether a human is needed, "
        "and whether a paid model is needed.\n\n"
        f"SITUATION:\n{situation}"
    )
    local = run_local(pool, situation, prompt, facts, model=model)
    if local is None:
        return escalate(
            "No standing rule matched and no loopback Ollama model is reachable.",
            facts=facts,
        )
    local["rule"] = None
    local["rule_id"] = None
    return local
