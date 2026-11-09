"""Retrieve vault facts and answer with a loopback model when one is up."""

from __future__ import annotations

from brain.ollama_client import OllamaPool
from brain.paths import vault_dir
from brain.retrieve import VaultIndex
from brain.router import base_result, escalate, run_local
from brain.rules import first_rule


def ask(
    question: str,
    k: int = 6,
    pool: OllamaPool | None = None,
    model: str | None = None,
) -> dict:
    vault = vault_dir()
    if vault.exists():
        index = VaultIndex.load(vault)
        hits = index.search(question, k=k, pool=pool)
    else:
        hits = []
    facts = [hit.as_dict() for hit in hits]
    rule = first_rule(question)
    rule_line = ""
    if rule:
        rule_line = f"Standing rule that matches: {rule.title}. {rule.ruling}"

    pool = pool or OllamaPool()
    prompt = (
        "You are Master Control for MedWave. Answer in four short lines using only the facts. "
        "Do not invent prices, emails, or phone numbers. "
        "If the facts are not enough, say what is missing.\n\n"
        f"QUESTION:\n{question}\n"
    )
    if rule_line:
        prompt += f"\n{rule_line}\n"
    local = run_local(pool, question, prompt, facts, model=model)
    if local is not None:
        if rule:
            local["rule"] = rule.title
            local["rule_id"] = rule.id
        return local

    # Rules-only. Retrieval still happened. Paid tokens only if no rule covers it.
    if rule:
        return base_result(
            route="rule",
            answer=rule.ruling,
            rule=rule.title,
            rule_id=rule.id,
            escalate_paid=False,
            escalate_human=rule.human,
            reason="Ollama is not reachable. Answered from the standing rule.",
            facts=facts,
        )
    return escalate(
        "Ollama is not reachable and no standing rule answers this.",
        facts=facts,
    )
