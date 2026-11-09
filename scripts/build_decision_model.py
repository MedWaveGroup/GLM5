#!/usr/bin/env python3
"""Builds decision-model.md, notes/index.md and manifest.json from local facts. Evidence is pulled by regex; gaps are marked OPEN."""
import json, re, os, glob, urllib.request
from datetime import date
BASE=os.environ.get('BRAIN_EXPORT', '/workspace/brain-export'); MODEL=os.environ.get('OLLAMA_MODEL','qwen2.5:3b')
F=json.load(open(f'{BASE}/raw/facts_tagged.json'))
def ev(rx, n=2, need=None):
    hits=[x for x in F if re.search(rx,x['text'],re.I) and (not need or re.search(need,x['text'],re.I))]
    hits.sort(key=lambda x:(x['kind']=='transcript', x['date']=='undated' or x['date']>str(date.today()), x['date']))
    return hits[:n]
def cite(rx, n=2, need=None):
    h=ev(rx,n,need)
    if not h: return '  - Evidence: **not found in this export — OPEN** (rule given in the brief; confirm with Davide).\n'
    return ''.join(f'  - Evidence ({x["date"]}, {x["source"]}): "{x["text"][:330]}{"…" if len(x["text"])>330 else ""}"\n' for x in h)
RULES=[
 ('Buyer rule: anyone with buying intent (price questions, "I want to start", ready to buy) is routed to Davide himself, not back to a setter or closer.', r'buyer rule|handles leads with buying intent himself|route buying intent to Davide', None),
 ('No SA pricing in writing before a sales call. Price questions get a call offer, not a number.', r'no SA pricing before|Pricing goes to Davide', None),
 ('Elmien is contacted on Slack only (never WhatsApp/SMS/email from the bots).', r'Elmien.{0,40}Slack only|Slack only.{0,40}Elmien|Elmien still Slack', None),
 ('Owned leads keep their owner; never reassign. Unowned leads go to Erich.', r'already have an owner|owner rule|never reassign|leads that already have an owner', None),
 ('Unowned leads default to Erich.', r'no clear owner are assigned to Erich|no owner.{0,40}Erich|unowned.{0,40}(go|default).{0,20}Erich', None),
 ('US outreach is email only (no SMS/WhatsApp consent in the US).', r'US is email.only|US outreach.{0,30}email|email.only.{0,30}US', None),
 ('Optimum panel only in aesthetics settings; Neuro in medical settings.', r'Optimum', r'aesthetic'),
 ('MedWave never pays leads\' travel or accommodation for events.', r'(travel|accommodation)', r'(never|not|no) .{0,40}(pay|cover)|pay.{0,30}(travel|accommodation)'),
 ('Every external send needs approval in Davide\'s own words; an agent relaying approval does not count.', r'own (approval|words)|approval in (his|Davide)|without his own approval', None),
 ('No HighLevel workflow is turned off without Sterrenberg or Francois.', r'(turn\w* off|disabl\w*|switch\w* off|pause\w*).{0,60}workflow|workflow.{0,80}(without|unless).{0,40}(Sterrenberg|Francois)', None),
 ('Bots report to Master Control, not to Davide; Davide only sees short bullets needing his decision.', r'report(s)? only to Master Control|none message him directly|short, easy-to-read bullet', None),
 ('Master Control escalates failures directly on Slack (bold, warnings, @-tags) without asking Davide first.', r'escalate and hold people accountable', None),
 ('Green/Amber decision tiers delegated to Master Control; Red stays with Davide; spend up to R5,000 without asking.', r'Green and Amber', None),
 ('Templates Master Control creates are named "Davide-Grok" / "davide_grok".', r'Davide-Grok', None),
 ('Token spend: fleet paused 6 Nov 19:11; only new-lead outreach and replies/booking continue. Full stop on 8 Nov evening; restart only Master Control and Outreach Control once the brain is set up (9 Nov).', r'paus\w+ (every|all) (bot|work)|token spend|overspending on tokens|Restart only Master Control', None),
]
HQ=[
 ('Definition (Davide, 1 Nov): any booking in the MedWave sales (closer) calendars counts as HQ unless it is a low-quality walkthrough webinar.', r'HQ booked appointment definition|automatically a high-quality|Definition of a high-quality appointment'),
 ('Brief definition: vetted by a BDR (Erich, Eddie, Michael, Hazel) AND booked into a salesperson\'s HighLevel calendar; "Bought" is the top tier.', r'vetted by a BDR'),
 ('Walkthrough-webinar bookings and Active Lifestyle Solutions (B2B partner) are NOT HQ.', r'Walkthrough.webinar bookings and Active Lifestyle'),
 ('Volume gate in the booking rules: group walkthrough first; closer one-to-ones only for practices seeing over 100 patients a month; 45-minute slots; no public holidays; notify the calendar owner.', r'over 100 patients|more than 100 patients|one-to-ones only'),
 ('Closer calendars: Andries (Discovery) and Elmien (Clinical / 1:1); Discovery round robin Andries/Elmien; Davide takes calls when closers are full.', r'Discovery round robin|Davide takes calls when|closers are Andries and Elmien'),
 ('Report every HQ booking with BOTH the setter and the calendar owner (Davide, 5 Nov 11:10).', r'who set the booking'),
 ('Targets: 20 HQ booked/day (no-show buffer), 2,000 outreach messages/day, 2 sales/day (40/month); setters 3–5 HQ each.', r'20 High Quality|20 high-quality \(HQ\)|5 per setter|3 HQ each'),
 ('Patients seeking personal treatment are not B2B leads: no closer booking; point to providers page (Master Control handling of Sandile Ndlovu, 8 Nov — Master Control practice, not a Davide ruling).', r'treat him as a patient|patient, not B2B'),
 ('Financing / try-before-you-buy only once patient volume is qualified (Objection bot playbook).', r'only once patient volume is qualified|try-before-you-buy \(only once'),
 ('Davide 9 Nov: Master Control decides lead quality from his past rulings and may book HQ leads directly into closer/sales calendars instead of walkthrough webinars.', r'may book high-quality leads directly'),
]
def ollama(p):
    body={'model':MODEL,'prompt':p,'stream':False,'options':{'temperature':0.1,'num_predict':450,'num_ctx':4096}}
    r=urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:11434/api/generate',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'}),timeout=600)
    return json.load(r)['response'].strip()
dec=[x for x in F if 'davide-decisions' in x['tags'] and x['kind']!='transcript']
sample='\n'.join(f'- ({x["date"]}) {x["text"][:220]}' for x in dec[:45])
try: patterns=ollama('Below are dated rulings by Davide, CEO of MedWave. List 8 short patterns in HOW he decides (what he prioritises, approves, kills). Only use what is shown; one line each.\n\n'+sample)
except Exception as e: patterns=f'(Ollama failed: {e})'
pb=os.environ.get('BRAIN_PLAYBOOK', os.path.join(BASE, 'raw/context_snapshot/DAVIDE_DECISION_PLAYBOOK.md'))
principles=''
if os.path.exists(pb):
    princ=re.search(r'## A\. Ten \*principles\*(.*?)\n## B\.', open(pb).read(), re.S)
    if princ:
        principles='\n'.join(l for l in princ.group(1).splitlines() if l.startswith('**'))
out=f'---\ntitle: "Davide decision model"\ntags: [medwave, brain, decision-model]\nsource: "facts_tagged.json (memory, transcripts, context docs); DAVIDE_DECISION_PLAYBOOK.md §A"\ndate: {date.today()}\n---\n\n# How Davide decides\n\nRelated: [[notes/davide-decisions]] · [[notes/standing-rules]] · [[notes/booking-and-calendars]] · [[notes/targets-kpis]] · [[notes/index]]\n\n'
out+='## 1. Priorities (from the playbook\'s ten principles, written by Master Control from his rulings)\n\n'+(principles or '_Principles section not found — OPEN_')+'\n\n'
out+='## 2. Standing rules and the evidence behind them\n\n'
for r,rx,need in RULES: out+=f'- **{r}**\n'+cite(rx,2,need)
out+='\n## 3. What he approves / what he kills (local pattern pass, '+MODEL+', unverified)\n\n'+patterns+'\n\nKnown kills from the record: JP Keyter path (6 Nov); "9 in 10 sales are Neuro-100S" and "best seller" claims (2 Nov). Known approvals: Green/Amber tiers (2 Nov), SA brochure health claims with Legal qualifiers (1 Nov), bulk texts to past bookers/event leads excl. opt-out/DND (1 Nov 21:27).\n\n'
out+='## 4. HQ lead-quality rubric: closer/sales calendar vs walkthrough webinar\n\nBuilt only from evidence in this export.\n\n### Evidence\n\n'
for r,rx in HQ: out+=f'- **{r}**\n'+cite(rx,1)
out+='''
### Rubric (apply in order)

1. **Buying intent** (asks price, "want to start", ready to order) → route to **Davide** (buyer rule). No written SA pricing. Book his call if he says so.
2. **Patient / personal-use only** (wants treatment for themselves, home device without practice) → **not HQ**. No closer booking; providers page or home-device path. Confirm before any sales nurture.
3. **Practice/clinic/gym owner or clinician, >100 patients a month** (or equivalent B2B scale, e.g. multi-booth recovery centre) → **book a closer 1:1** (Andries Discovery / Elmien Clinical, 45 min, earliest slot ideally within 3 days, no public holidays), owner unchanged, notify calendar owner, report setter + calendar owner. Counts as HQ.
4. **B2B but volume unknown or under 100 patients/month, or unsure** → **group walkthrough webinar** first (not HQ), BDR qualifies volume, then upgrade to closer if rule 3 is met.
5. **B2B partner/distributor deals** (e.g. Active Lifestyle Solutions) → partnership track (Radar), not HQ.
6. **Excluded always:** opted-out, DND, closed-lost, already messaged today, existing customers for sales outreach.

### Gaps (OPEN — need Davide)

- No explicit rule on decision-maker vs employee, budget/finance readiness, or timeline as HQ signals.
- Whether Davide's 9 Nov "book directly when they seem high quality" relaxes the >100 patients/month gate, or keeps it.
- Aesthetics leads: whether Optimum-panel leads (no patient-count concept) use the same 100/month gate.
- US leads: no evidence of which sales calendar or closer handles US bookings (US is email-only).
- How to split new HQ bookings between Andries and Elmien beyond round robin; when Davide's own calendar is used.
- Whether "walkthrough-only" past attendees who reply positively can go straight to a closer.
'''
open(f'{BASE}/decision-model.md','w').write(out)
# index
notes=sorted(os.path.basename(p)[:-3] for p in glob.glob(f'{BASE}/notes/*.md') if not p.endswith('index.md'))
st=json.load(open(f'{BASE}/raw/build_stats.json'))
idx=f'---\ntitle: "MedWave brain index"\ntags: [medwave, brain, index]\nsource: "brain-export build"\ndate: {date.today()}\n---\n\n# MedWave brain index\n\nOne-time export ({date.today()}) of what the MedWave bot fleet has learned. Built locally with Ollama ({MODEL}) and Headroom; see `manifest.json` for sources and token-using calls.\n\n## Notes\n\n'
for n in notes: idx+=f'- [[{n}]] ({st["note_counts"].get(n,"-")} items)\n'
idx+='- [[../decision-model|decision-model]]: how Davide decides + HQ lead rubric\n\n## How to use\n\n- Rulings with dates: [[davide-decisions]]. Hard rules: [[standing-rules]].\n- Booking a lead: [[booking-and-calendars]] then the HQ rubric in decision-model.\n- Who is who: [[team]], [[bots]].\n- Facts carry a `_source_` line; transcript snippets are undated search excerpts.\n'
open(f'{BASE}/notes/index.md','w').write(idx)
print('ok')
