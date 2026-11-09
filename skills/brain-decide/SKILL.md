---
name: brain-decide
description: Use when Master Control must rule on a situation the way Davide would, citing the standing rule and saying whether a paid model or Davide himself is required.
---

# Brain decide

## Rule

Local first, tokens last.

1. Apply `decision-model.md` and the standing rules with no model call.
2. If no rule matches, ask the loopback Ollama model.
3. Set `escalate_paid` only when no rule matched and no local model answered, or the local model was uncertain. Set `escalate_human` when the item is Red, over R5,000, an external send, or an open gap. A human flag means Davide, not a bigger model.

## Commands

```bash
brain decide "A lead came in with no owner"
brain decide "They asked how much it costs on WhatsApp"
brain decide "Turn off the HighLevel nurture workflow"
brain decide "Approve R8000 of ad spend" --json
```

Read the ruling, the cited rule, `Paid model needed`, and `Human needed`.
