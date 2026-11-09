"""Task assignment entry. Rule, then local model, then the paid flag."""

from __future__ import annotations

from brain.assign import assign_rule, assignment_dict
from brain.ollama_client import OllamaPool
from brain.router import escalate, run_local
from brain.decide import _facts


def assign(task: str, pool: OllamaPool | None = None, model: str | None = None) -> dict:
    item = assign_rule(task)
    if item is not None:
        result = assignment_dict(item)
        result["facts"] = _facts(task, limit=3)
        result["answer"] = f"{item.owner}: {item.next_step}"
        return result

    facts = _facts(task, limit=4)
    pool = pool or OllamaPool()
    prompt = (
        "You are Master Control. Name one owner and one next step for this MedWave task. "
        "Use only the facts. If you cannot tell, say you do not know.\n\n"
        f"TASK:\n{task}"
    )
    local = run_local(pool, task, prompt, facts, model=model)
    if local is None:
        result = escalate(
            "No assignment rule matched and no loopback Ollama model is reachable.",
            facts=facts,
        )
        result["owner"] = None
        result["next_step"] = None
        return result
    local["owner"] = None
    local["next_step"] = local["answer"]
    return local
