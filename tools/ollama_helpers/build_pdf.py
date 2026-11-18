"""Build MedWave_Knowledge_Base_2026-11-12.pdf from KNOWLEDGE_BASE_TRUNCATED.md (+ flow.png)."""
import pathlib, markdown
from weasyprint import HTML
root = pathlib.Path(__file__).resolve().parents[2] / "docs"
md = (root / "KNOWLEDGE_BASE_TRUNCATED.md").read_text()
body = markdown.markdown(md, extensions=["tables", "sane_lists"])
STEPS = [
 ("det", "1 · Intake", "HighLevel reply · website form · reactivation list · Slack request"),
 ("det", "2 · Privacy scrub", "privacy_scrub.py: no phones, emails, tokens or webhook URLs in any prompt"),
 ("det", "3 · Hard filters", "STOP / opt-out / DND · already booked · US = email only · auto-reply  →  drop + log"),
 ("oll", "4 · Classify (Ollama)", "qwen2.5 on 127.0.0.1:11434 · label + confidence · classify_reply.py"),
 ("det", "5 · Brain lookup", "GLM5 decide / triage-lead / assign / ask · BM25 over the vault"),
 ("oll", "6 · Template or Ollama draft", "approved wording first (finance_quote.py for monthly figures) · else Ollama draft after Headroom"),
 ("det", "7 · Compliance + dedupe gate", "compliance_gate.py · dedupe_wording.py (Ollama only in the grey band) · block → retry locally once"),
 ("paid", "8 · Escalate to paid model ONLY IF", "Ollama down · confidence &lt; 0.6 · lead-specific wording / new objection · 2 failed local drafts · needs HighLevel/calendar tools · long synthesis"),
 ("det", "9 · Send gates", "email ≤ 50/day · 24h skip for blasts &amp; reactivation (1h new-lead re-touch exempt) · ≤ 3 touches/day · CPD no price before event · monthly price only · no repeat wording · 09:00–10:59"),
 ("hum", "10 · Human gate", "buyer · Red item · spend &gt; R5,000 · new external send type → Davide card · owner nudge (Elmien on Slack)"),
 ("det", "11 · Send", "HighLevel, WhatsApp first · tag davide-bot-outreach"),
 ("det", "12 · Log", "sends_log.csv · savings.jsonl · OC FYI with contactIds → Master Control"),
 ("oll", "13 · Digest (Ollama)", "summarise.py → short MC bullets for Davide"),
]
flow = "".join(f'<div class="st {k}"><b>{t}</b><span>{d}</span></div><div class="ar">▼</div>' for k,t,d in STEPS)
flow = flow.rsplit('<div class="ar">▼</div>',1)[0]
body += ('<h2 class="pb">Appendix: the Ollama-first process flow</h2>'
         '<p class="legend"><i class="det"></i>Deterministic rule or script <i class="oll"></i>Local Ollama '
         '<i class="paid"></i>Paid model (last resort) <i class="hum"></i>Davide or a human owner</p>'
         f'<div class="flow">{flow}</div>'
         '<p class="small">Mermaid source and the full stage table are in <code>PROCESS_FLOW.md</code>. Live send paths and the Mac watcher are unchanged.</p>')
css = """
@page { size: A4; margin: 16mm 15mm 16mm 15mm;
  @bottom-left { content: "MedWave · Knowledge base · 12 Nov 2026 · Internal"; font: 8pt 'DejaVu Sans'; color:#7a8794 }
  @bottom-right { content: counter(page) " / " counter(pages); font: 8pt 'DejaVu Sans'; color:#7a8794 } }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 9.3pt; line-height: 1.42; color:#1d2733 }
h1 { font-size: 20pt; color:#0b3d5c; margin:0 0 4pt; border-bottom: 3pt solid #c8102e; padding-bottom:5pt }
h2 { font-size: 12.5pt; color:#fff; background:#0b3d5c; padding:4pt 8pt; margin:13pt 0 6pt; border-radius:3pt; page-break-after: avoid }
h2.pb { page-break-before: always }
p, li { margin: 2pt 0 }
ul, ol { margin: 3pt 0 5pt 0; padding-left: 15pt }
table { border-collapse: collapse; width:100%; margin:5pt 0 8pt; font-size: 8.6pt; page-break-inside: avoid }
th { background:#e6eef4; color:#0b3d5c; text-align:left; padding:3.5pt 5pt; border:0.6pt solid #b8c7d3 }
td { padding:3pt 5pt; border:0.6pt solid #cfd9e1; vertical-align: top }
tr:nth-child(even) td { background:#f6f9fb }
code { font-family:'DejaVu Sans Mono', monospace; font-size:8pt; background:#eef2f5; padding:0 2pt; border-radius:2pt }
strong { color:#0b3d5c }
hr { border:0; border-top:0.8pt solid #cfd9e1; margin:8pt 0 }
blockquote { border-left:3pt solid #c8102e; margin:4pt 0; padding:2pt 8pt; color:#3c4a57 }
.legend { font-size:8.3pt } .legend i { display:inline-block; width:9pt; height:9pt; border-radius:2pt; margin:0 3pt 0 9pt; vertical-align:middle }
.flow { margin-top:4pt } .st { border-radius:4pt; padding:4pt 9pt; border:0.8pt solid; page-break-inside:avoid }
.st b { display:block; font-size:9.6pt } .st span { font-size:8.4pt; color:#33414e }
.ar { text-align:center; color:#7a8794; font-size:7pt; line-height:9pt; margin:0 }
.det, i.det { background:#eef2f5; border-color:#9fb1c0 } .oll, i.oll { background:#e3f4e8; border-color:#4f9d69 }
.paid, i.paid { background:#fff3dc; border-color:#d99a22 } .hum, i.hum { background:#fde7ea; border-color:#c8102e }
.small { font-size:8pt; color:#5a6874; margin-top:6pt }
img.flow { display:block; margin: 4pt auto 0; max-height: 228mm; max-width: 100% }
"""
html = f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"
out = root / "MedWave_Knowledge_Base_2026-11-12.pdf"
HTML(string=html, base_url=str(root)).write_pdf(out)
print(out)
