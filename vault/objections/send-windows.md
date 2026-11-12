---
title: "24-hour skip for blasts and reactivation; 1-hour re-touch; no repeated wording"
tags: [medwave, brain, objections, standing-rules, rule]
source: "Davide Duranti, 12 Nov 2026 10:21–10:25 SAST, relayed by Master Control"
date: 2026-11-12
---

# 24-hour skip for blasts and reactivation; 1-hour re-touch; no repeated wording

Davide, 12 Nov 2026 (10:21 clarification at 10:22, sequence tags at 10:25 SAST).

## 24-hour any-communication skip (blasts and reactivation only)

- Before any blast, reactivation or follow-up send that is a blast or a reactivation, skip anyone who received any message from MedWave in the last 24 hours (bot, BDR or closer, any channel).
- Check HighLevel conversation history, not only our own send logs.
- The daily quiet-lead batch is treated as reactivation, so the 24-hour skip applies to it.
- The existing 48-hour skip for reactivation stays in force and is stricter: if they were reached in the last 48 hours, skip the reactivation send.
- Do not apply this 24-hour skip to the 1-hour re-touch of brand-new leads who have not replied.

## 1-hour re-touch for brand-new unreplied leads

- The 1-hour re-touch cadence stays on for brand-new leads who have not replied.
- At most 3 automated touches a day.
- Each touch must add something new.
- Stop on reply, booking, opt-out, or owner pickup.
- The 24-hour any-communication skip does not apply to this cadence.

## Never repeat wording (every send, including re-touches)

- Never send a contact the same or near-identical wording twice.
- Compare the proposed text against their past outbound messages in HighLevel.
- This applies to every send, including 1-hour re-touches, which matches "each adding something new".

## Sequence tags N1 and B1–B5

- Sequence membership is shown only by the sequence tag on the HighLevel contact. Detect it from the tags, not from a spreadsheet guess.
- Exact sequence tag names found in HighLevel (SA location, 12 Nov 2026): `n1`, `n1 - b5`, `b1`, `b1 - b5`, `b2`, `b3`, `b4`, `b5`.
- If a contact has one of those tags and was contacted in the last 24 hours, pause sequence messaging.
- If they reply, book immediately (discovery call rules).
- `wa-react-1112-b1` is a 12 Nov reactivation batch tag, not an N1/B1–B5 sequence tag.

## Source and date

- 24-hour skip and no repeated wording: Davide Duranti, 12 Nov 2026 10:21 SAST, corrected 10:22 SAST (24h is blasts and reactivation only; re-touch cadence stays).
- Sequence tags, pause if contacted in the last 24 hours, book immediately on reply: Davide Duranti, 12 Nov 2026 10:25 SAST.

Related: [[guardrails]] · [[cpd-no-pricing]] · [[standing-rules]] · [[davide-decisions]] · [[Start here]]
