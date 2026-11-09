"""Routing order: deterministic rule, then loopback Ollama, then paid-model flag."""

from __future__ import annotations

import json
import re

from brain.headroom_util import compress_context
from brain.ollama_client import OllamaPool

_UNCERTAIN = re.compile(
    r"\b(i don't know|i do not know|not enough information|cannot determine|can't determine|"
    r"need more context|unsure|no evidence)\b",
    re.I,
)


def base_result(**extra) -> dict:
    result = {
        "route": "rule",
        "answer": "",
        "rule": None,
        "rule_id": None,
        "escalate_paid": False,
        "escalate_human": False,
        "reason": None,
        "facts": [],
        "model": None,
        "host": None,
    }
    result.update(extra)
    return result


def escalate(reason: str, facts: list | None = None, human: bool = False) -> dict:
    return base_result(
        route="escalate",
        answer="",
        escalate_paid=not human,
        escalate_human=human,
        reason=reason,
        facts=facts or [],
    )


def run_local(
    pool: OllamaPool,
    question: str,
    prompt: str,
    facts: list[dict],
    system: str | None = None,
    model: str | None = None,
) -> dict | None:
    """Call a loopback model on a Headroom-shrunk prompt. None if no host answers."""
    payload = json.dumps(facts, ensure_ascii=False)
    shrunk = compress_context(question, payload)
    full = prompt
    if shrunk:
        full = prompt.rstrip() + "\n\nFACTS:\n" + shrunk
    generated = pool.generate(full, system=system, model=model)
    if not generated:
        return None
    text = generated["text"]
    uncertain = bool(_UNCERTAIN.search(text))
    return base_result(
        route="local",
        answer=text,
        escalate_paid=uncertain,
        escalate_human=False,
        reason="Local model was uncertain, so a paid model should confirm." if uncertain else None,
        facts=facts,
        model=generated["model"],
        host=generated["host"],
    )
