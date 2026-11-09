---
name: brain-ask
description: Use when Master Control needs a sourced answer from the MedWave vault, such as who owns a lead, what Davide ruled, or which product fits a setting. Local model first; paid tokens only if the command sets escalate_paid.
---

# Brain ask

## Rule

Local first, tokens last.

1. A deterministic rule or a vault lookup answers when it can.
2. Otherwise a loopback Ollama model answers (`qwen2.5:7b` on Davide's Mac, `qwen2.5:3b` on the Linux box).
3. A paid model runs only when the command sets `escalate_paid` to yes, and the reason says why.

Do not tunnel Ollama. Both hosts are `http://127.0.0.1:11434`.

## Commands

```bash
brain ask "Who gets unowned leads?"
brain ask "Is Elmien on WhatsApp or Slack?" --json
brain ask "What did Davide rule about SA pricing?" --model qwen2.5:7b
```

The reply lists the top facts with their `_source_` lines. If Ollama is down and a standing rule covers the question, the route is `rule` and no paid model is needed.
