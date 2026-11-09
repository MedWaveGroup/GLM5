---
name: task-assign
description: Use when a task needs the simplest owner and one next step, such as an unowned lead, a HighLevel workflow, an installation, a referral, or a report.
---

# Task assign

## Rule

Local first, tokens last.

1. The first matching standing rule names one owner and one next step. No model call.
2. If nothing matches, ask the loopback Ollama model.
3. A paid model is used only when `escalate_paid` is yes. External sends and spend above R5,000 set `escalate_human` and go to Davide.

## Commands

```bash
brain assign "new lead with no owner"
brain assign "turn off the HighLevel workflow"
brain assign "book the installation for Friday"
brain assign "chase the missed HQ target" --json
```

Read `Owner` and `Next step`.
