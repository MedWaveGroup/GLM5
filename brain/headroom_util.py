"""Shrink fact context with Headroom when the package is installed.

`compress()` is optional. A missing package or a failed call returns the
original text so the CLI still runs.
"""

from __future__ import annotations

import json


def compress_context(question: str, payload: str) -> str:
    """Return a smaller payload when Headroom is available, else `payload`."""
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
        result = compress(messages, model="gpt-4o")
    except Exception:
        return payload
    try:
        produced = result.messages if hasattr(result, "messages") else result["messages"]
        content = produced[2]["content"]
    except Exception:
        return payload
    if content is None or content == "":
        return payload
    if isinstance(content, str):
        return content
    try:
        return json.dumps(content, ensure_ascii=False)
    except Exception:
        return payload
