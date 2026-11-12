"""Shrink fact context with Headroom when the package is installed.

`compress()` is optional. A missing package or a failed call returns the
original text so the CLI still runs.

Important: never return CCR stubs (`<<ccr:…>>`) to Ollama — the local model
cannot call headroom_retrieve, so stubs drop the facts the answer needs.
"""

from __future__ import annotations

import json


def _looks_like_ccr_stub(content: str) -> bool:
    return "<<ccr:" in content


def compress_context(question: str, payload: str) -> str:
    """Return a smaller payload when Headroom is available, else `payload`.

    Uses Headroom's JSON-friendly path (smart crusher). Does not force a
    Kompress target_ratio that can replace facts with CCR stubs. If the
    result is a stub or empty, the original payload is kept.
    """
    if not payload:
        return payload
    try:
        from headroom import compress
    except Exception:
        return payload
    messages = [
        {"role": "user", "content": question},
        {
            "role": "assistant",
            "content": None,
            "tool_calls": [
                {
                    "id": "c1",
                    "type": "function",
                    "function": {"name": "facts", "arguments": "{}"},
                }
            ],
        },
        {"role": "tool", "tool_call_id": "c1", "content": payload},
        {"role": "user", "content": question},
    ]
    try:
        # No target_ratio / kompress_model: JSON facts go through smart_crusher
        # (~0.6 keep) and retain Erich / pricing / Optimum wording.
        result = compress(messages, model="gpt-4o", min_tokens_to_compress=50)
    except Exception:
        return payload
    try:
        produced = result.messages if hasattr(result, "messages") else result["messages"]
        content = produced[2]["content"]
    except Exception:
        return payload
    if content is None or content == "":
        return payload
    if not isinstance(content, str):
        try:
            content = json.dumps(content, ensure_ascii=False)
        except Exception:
            return payload
    if _looks_like_ccr_stub(content):
        return payload
    # If somehow larger or empty of key substance, keep original
    if len(content) < 20:
        return payload
    return content
