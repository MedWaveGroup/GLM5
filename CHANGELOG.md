# Changelog

## 2026-11-12: Knowledge base, Ollama-first process flow and gap fixes

**Added**
- `docs/KNOWLEDGE_BASE_TRUNCATED.md` and `docs/MedWave_Knowledge_Base_2026-11-12.pdf`: a short operating knowledge base covering core rules, the bot roster and reporting lines, the lead lifecycle, pricing, contact rules, booking, routing, escalation and security.
- `docs/PROCESS_FLOW.md` and `docs/flow.png`: the Ollama-first flow (intake → scrub → hard filters → Ollama classify → brain → template or Ollama draft → compliance/dedupe gate → paid escalation trigger → send gates → human gate → send → log → Ollama digest).
- `docs/OLLAMA_GAP_ANALYSIS.md`: 19 tasks mapped to their current engine, whether Ollama can do them, the gap, and the fix.
- `tools/ollama_helpers/` (loopback-only, no sends, no HighLevel calls):
  - `ollama_local.py`: client that refuses non-loopback hosts and logs estimated tokens saved.
  - `compliance_gate.py`: pre-send gate covering the CPD no-pricing rule, the full-price ban, rate/term/deposit wording, US email-only, the 50-a-day email cap, 3 touches a day, the 24-hour rule for blasts and reactivation (1-hour new-lead re-touch exempt), sign-off and "reply stop" checks, repeated wording, and the `davide-bot-outreach` tag.
  - `dedupe_wording.py`: repeated-wording check, deterministic with an Ollama grey band.
  - `classify_reply.py`: regex first, then Ollama. Adds the `price_question` and `area_objection` labels.
  - `summarise.py`: scrub → Ollama bullets → scrub. Refuses `brain-export/raw/` and `context/confidential/`.
  - `finance_quote.py`: 11%/60-month amortisation and the approved monthly figures (R2,174 / R3,805 / R4,131 / R5,436 / R8,153), with lead-facing lines that mention no rate or term.
  - `privacy_scrub.py`: redacts emails, phones, JIDs, tokens, JWTs and webhook URLs; `--check` mode.
  - `selftest.py`: 14 offline tests.

**Rules recorded (Davide, 12 Nov 2026)**
- CPD-tagged doctors get no pricing until `cpd - attended`.
- Only monthly finance amounts go to leads, never full prices.
- Email capped at 50 a day; volume goes on WhatsApp.
- Tag `davide-bot-outreach` on every bot-messaged contact.
- Blasts and reactivation skip anyone contacted in the last 24 hours; the 1-hour re-touch for brand-new leads stays.
- No repeated wording to the same contact.

**Not changed**
- Live send paths, the Mac reply watcher and HighLevel workflows.

**Pending**
- Patient price wording (monthly version) awaits Davide's confirmation.
- `nomic-embed-text` pull failed on the box (registry unreachable).
