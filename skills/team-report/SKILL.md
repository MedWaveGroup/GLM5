---
name: team-report
description: Use when Master Control needs the daily team-performance skeleton against 20 HQ bookings, 2,000 WhatsApps, and 2 sales. Fill actuals when they are known.
---

# Team report

## Rule

Local first, tokens last. The skeleton is a lookup of Davide's engine-room targets. It does not call a model and it does not spend tokens.

Targets: 20 HQ bookings a day, 2,000 WhatsApps a day, 2 sales a day (40 a month). Setters are Erich, Eddie, Michael, and Hazel at 3 to 5 HQ each. Closers are Andries (Discovery) and Elmien (Clinical). Report every HQ booking with both the setter and the calendar owner.

## Commands

```bash
brain report
brain report --hq 10 --whatsapps 1500 --sales 1
brain report --numbers '{"hq": 10, "whatsapps": 1800, "sales": 2}' --json
```

A blank actual means the number was not provided. Do not invent one.
