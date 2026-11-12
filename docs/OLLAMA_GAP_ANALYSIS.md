# Ollama gap analysis (12 Nov 2026)

**Ollama check, 12 Nov 2026 about 10:25 SAST:** `curl 127.0.0.1:11434/api/tags` on the box answered. It has one model, **`qwen2.5:3b`** (3.4B, Q4_K_M, 32k context). A "say OK" call returned in about 6.7 s. Summarising a 4–9 KB file took 30–190 s.
**Not installed:** `nomic-embed-text`, so GLM5's `ask` rerank falls back to plain BM25. `ollama pull nomic-embed-text` was tried and failed: the registry could not be reached from the box ("max retries exceeded"). Mac models were not checked, because the Mac's Ollama is loopback-only and can't be reached from the box by design.
**Watcher evidence:** the Mac reply watcher's local backtest (`backtest_local_replies_results.json`) passed 12 of 12 cases, and 4 of them were correctly escalated.

**Key:** ✅ filled today (box, low risk) · 🟡 proposed (needs OC, a repo change, or Davide) · ⚪ already Ollama-first

| # | Task | Current engine | Can Ollama do it? | Gap | Fix |
|---|---|---|---|---|---|
| 1 | Inbound reply classification (Mac watcher) | Regex + Ollama | Yes | None in the engine. It has no `price_question` or `area_objection` label, so the CPD and area rules are only enforced downstream. | ⚪ in place. 🟡 Add the two labels from `tools/ollama_helpers/classify_reply.py` to the watcher's `classify.py` (OC owns this; the Mac watcher was not changed). |
| 2 | Standard replies (value gives, booking confirmations, declines) | Ollama + fixed templates (approved 9 Nov) | Yes | None | ⚪ in place |
| 3 | New website-lead triage (box watcher) | Deterministic + Ollama | Yes | None | ⚪ in place |
| 4 | **Pre-send compliance check**: CPD no-pricing, full-price ban, rate/term/deposit, US channel, email cap, 3 touches a day, sign-off, "reply stop" | MC/OC reading by hand (paid tokens) | Yes for tone. The rules themselves are deterministic. | No automated gate. Today's CPD and finance-only rulings rely on bots remembering them. | ✅ `tools/ollama_helpers/compliance_gate.py`, plus 14 offline tests in `selftest.py`. Advisory only. 🟡 OC to call it in the batch builders before each send. |
| 5 | **Repeated-wording dedupe** | None or by hand | Yes, in the grey band | Nothing stopped the same opener going to the same contact twice | ✅ `tools/ollama_helpers/dedupe_wording.py`: shingle and difflib check, with Ollama judging the 0.55–0.80 band |
| 6 | **24-hour no-contact check for blasts and reactivation** | OC batch scripts (48h for WhatsApp reactivation) | Deterministic | No shared check for other blasts. The 1-hour re-touch must stay exempt. | ✅ in `compliance_gate.py` (campaign-aware). 🟡 It needs HighLevel last-message times passed in, because Ollama can't call HighLevel. |
| 7 | **Finance monthly maths** | Paid model by hand | Deterministic, no model needed | Paid tokens spent on arithmetic, and a risk of drifting figures | ✅ `tools/ollama_helpers/finance_quote.py` (formula, approved figures and lead-facing lines with no rate or term) |
| 8 | **Summaries for KBs, Slack digests, OC response reports, MC bullets** | Paid model | Yes for extraction; the 3B model is weak at synthesis | Most report and digest writing still uses paid tokens | ✅ `tools/ollama_helpers/summarise.py` (scrub, chunk, Ollama, scrub). It drafted 5 sections of this KB (`ollama_drafts/`). 🟡 OC and Communication bot to use it for response reports and Slack digests. |
| 9 | **Privacy scrub before prompts and repo pushes** | GLM5 `privacy.py` (tests only) | Deterministic | No pre-prompt or pre-commit scrub for ad-hoc files. Some team files contain phone numbers. | ✅ `tools/ollama_helpers/privacy_scrub.py` (`--check` for CI or pre-commit; keeps dates and amounts) |
| 10 | Objection replies | Ollama draft, then a paid rewrite | Partly. 3B output was generic and invented claims (12 Nov area objection). | Free-form drafting isn't reliable on 3B | 🟡 Have Ollama **pick** from the approved objection library (classification, not writing). Paid only for new objections. Use the Mac's 7B for free drafts. |
| 11 | Wording Lab variants | Paid model | Partly | All variant generation uses paid tokens | 🟡 Ollama (Mac 7B) writes 5 variants, `compliance_gate.py` filters them, and a paid model or a human picks one |
| 12 | Pre-call brief | HighLevel MCP pull (paid agent) + `brief.py` formatter | Partly. The thread summary can be local; the HighLevel pull can't. | The thread summary is written with paid tokens | 🟡 Pipe the pulled `messages` through `summarise.py --focus "what the lead wants, objections, next step"` before `brief.py`. The brief still goes to Davide only. |
| 13 | Batch list building and exclusions (reengage, OC CSVs) | Ad-hoc Python written by the paid agent each run | Not a model task | Paid tokens spent rewriting similar scripts every day | 🟡 Make one reusable queue builder that calls `compliance_gate.py` per row (OC owns it) |
| 14 | HighLevel reads and writes (contacts, tags, conversations, bookings) | MCP through the paid agent | **No.** Ollama has no tool access. | Unavoidable paid step | 🟡 Leave as is, or script reads with the watcher's `hl_client` on the Mac. That touches the token env, so it needs Davide's OK. |
| 15 | Booking slot selection | Paid agent + calendar MCP | Deterministic once free/busy is fetched | Paid tokens spent on slot logic | 🟡 Slot picker for :00/:30 starts, 45 minutes free, no double-booking, Elmien/Davide first then Andries (most open slots) |
| 16 | GLM5 brain rules for 11–12 Nov | `brain/rules.py` | Deterministic | The 12 Nov cards (`cpd-no-pricing`, `monthly-prices-only`, `blast-reactivation-24h-skip`, `no-duplicate-wording`, `new-lead-one-hour-retouch`, `sequence-n1-b1-b5`) were previously uncommitted in the local clone | ✅ Committed on this branch in `Record 12 Nov standing rules in the manager brain`. |
| 17 | Embedding rerank for `brain ask` | BM25 only | Yes, with `nomic-embed-text` | Model not installed | 🟡 `ollama pull nomic-embed-text` on the Mac (box pull failed: registry unreachable) |
| 18 | Headroom prose compression | Headroom `compress()` with no `target_ratio`, so Kompress does nothing | Local, no model | Less compression than planned | ✅ The `target_ratio` change is in `brain/headroom_util.py` on this branch (same 12 Nov rules commit). |
| 19 | Mac-vs-box model size | Box has 3B only | — | Heavy local drafting on the box is slow and weaker | 🟡 Route long summaries and free drafting to the Mac's 7B when Davide's Mac is on |

## Top gaps and status

1. **No automated pre-send gate for today's rules** (CPD, finance only, 24 hours, email cap, repeated wording). **Filled** with `compliance_gate.py` and `dedupe_wording.py`, as an advisory tool. Wiring them in is OC's next step.
2. **Reports, digests and KB writing on paid tokens.** **Filled** with `summarise.py`, which was used for this KB.
3. **Finance figures done by hand.** **Filled** with `finance_quote.py`.
4. **Privacy scrub before prompts and pushes.** **Filled** with `privacy_scrub.py`.
5. **Objection and Wording Lab drafting.** **Proposed**: Ollama picks from the library or generates variants for the gate to filter. 3B isn't reliable enough to write them alone.
6. **HighLevel and calendar tool calls.** Can't move to Ollama, which has no tool access. They stay paid.

## Measured today (box, qwen2.5:3b)

- 3 replies classified correctly (price question, area objection, STOP; the STOP was caught by regex, not the model) in about 8 s total.
- The `send_rules.md` summary (10 bullets) took 31 s and kept every rule exact.
- The `lead-handling` summary (25 bullets) was noisy and mixed in older items. It needed MC editing. This is evidence for trigger 6, "synthesis over about 6k chars".
- Every helper call logs estimated paid tokens avoided to `tools/ollama_helpers/savings_helpers.jsonl`.
