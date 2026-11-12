# Ollama helper scripts (12 Nov 2026)

These live in `tools/ollama_helpers/`. They are box-side helpers. They use loopback-only Ollama (`127.0.0.1:11434`), and `ollama_local.py` refuses any other host. They never send messages, never call HighLevel and never read secrets. When Ollama is down they fall back to deterministic logic or return `escalate_paid`.

| Script | What it does |
|---|---|
| `ollama_local.py` | Client: picks `qwen2.5:7b` if it's installed (Mac), otherwise `qwen2.5:3b` (box). Logs estimated tokens saved to `savings_helpers.jsonl`. |
| `compliance_gate.py` | Pre-send gate. Takes a JSON object or a list and returns pass, blocks, warns, `tags_to_add` and the engine used. |
| `dedupe_wording.py` | Repeated-wording check (shingles and difflib; Ollama in the 0.55–0.80 grey band). |
| `classify_reply.py` | Regex first (STOP, auto-reply), then an Ollama label. Adds `price_question` and `area_objection`. |
| `summarise.py` | Scrub → chunk → Ollama bullets → scrub. Refuses `brain-export/raw/` and `context/confidential/`. |
| `finance_quote.py` | 11%/60-month maths and the approved lead-facing monthly lines. |
| `privacy_scrub.py` | Redaction filter. `--check FILE` exits 1 if it finds anything. |
| `build_pdf.py` | Rebuilds the knowledge-base PDF. |
| `selftest.py` | 14 offline tests. Ollama is not needed. |

```bash
python3 selftest.py
echo '{"text":"About R4,131 a month, excluding VAT. Would that work?","channel":"whatsapp","tags":["cpd opt-in"],"campaign":"reply"}' | python3 compliance_gate.py
python3 classify_reply.py --text "How much is it per month?"
python3 summarise.py some_notes.md --bullets 8 --focus "contact rules"
python3 finance_quote.py --lines
```

Wiring `compliance_gate.py` into OC's batch builders is OC's job. It is not done here, and live send paths are unchanged.
