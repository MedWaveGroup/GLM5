#!/usr/bin/env python3
"""Local brain builder: parses raw dumps, redacts, dedupes, tags (keywords + Ollama),
compresses with Headroom, summarises with Ollama, writes Obsidian notes.
No cloud LLM calls. Run with ~/hr-venv/bin/python."""
import json, re, glob, os, difflib, time, urllib.request, sys
from datetime import date
BASE = os.environ.get('BRAIN_EXPORT', '/workspace/brain-export')
RAW = f'{BASE}/raw'; NOTES = f'{BASE}/notes'
MODEL = os.environ.get('OLLAMA_MODEL', 'qwen2.5:3b')
OLLAMA = 'http://127.0.0.1:11434/api/generate'
TODAY = date.today().isoformat()
STATS = {'ollama_calls': 0, 'ollama_seconds': 0.0, 'headroom': []}

# ---------- redaction ----------
SECRET_RX = [r'sk_(live|test)_[A-Za-z0-9]+', r'xox[abposr]-[A-Za-z0-9-]+', r'gh[pousr]_[A-Za-z0-9]{20,}',
             r'Bearer\s+[A-Za-z0-9._-]+', r'(?i)(api[_-]?key|token|secret|password)\s*[:=]\s*\S+', r'AIza[0-9A-Za-z_-]{20,}']
def redact(t):
    t = re.sub(r'</?cursor_untrusted_data[^>]*>', '', t)
    for rx in SECRET_RX: t = re.sub(rx, '[secret-redacted]', t)
    t = re.sub(r'[\w.+-]+@[\w-]+\.[\w.-]+', '[email]', t)
    t = re.sub(r'(?<![\w.])\+?\d[\d\s()-]{8,}\d(?![\w.])', lambda m: m.group(0) if re.fullmatch(r'\d{10}\.\d+', m.group(0)) else '[phone]', t)
    t = re.sub(r'\b0[1-8][0-9]{8}\b', '[phone]', t)
    t = re.sub(r'@lid\b', '', t)
    return t.strip()

# ---------- ollama ----------
def ollama(prompt, num_predict=300, system=None):
    body = {'model': MODEL, 'prompt': prompt, 'stream': False, 'options': {'temperature': 0.1, 'num_predict': num_predict, 'num_ctx': 4096}}
    if system: body['system'] = system
    t0 = time.time()
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode(), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=600) as r: out = json.load(r)['response']
    STATS['ollama_calls'] += 1; STATS['ollama_seconds'] += time.time() - t0
    return out.strip()

# ---------- headroom ----------
def headroom_compress(items, label, question):
    """Compress a JSON list of facts with Headroom SmartCrusher; returns (list, before, after)."""
    try:
        from headroom import compress
        msgs = [{"role": "user", "content": question},
                {"role": "assistant", "content": None, "tool_calls": [{"id": "c1", "type": "function", "function": {"name": "facts", "arguments": "{}"}}]},
                {"role": "tool", "tool_call_id": "c1", "content": json.dumps(items)},
                {"role": "user", "content": question}]
        r = compress(msgs, model="gpt-4o")
        out = r.messages[2]['content']
        try: lst = json.loads(out)
        except Exception: lst = out
        STATS['headroom'].append({'label': label, 'tokens_before': r.tokens_before, 'tokens_after': r.tokens_after, 'transforms': r.transforms_applied})
        return lst
    except Exception as e:
        STATS['headroom'].append({'label': label, 'error': str(e)[:200]}); return items

# ---------- parse sources ----------
facts = []
def add(text, date_, source, kind, bot=None):
    text = redact(text)
    if len(text) < 25: return
    facts.append({'text': text, 'date': date_, 'source': source, 'kind': kind, 'bot': bot})

for f in sorted(glob.glob(f'{RAW}/memory/*.txt')):
    for l in open(f):
        m = re.match(r'- \((\d{4}-\d\d-\d\d)\) \[([^\]]+)\] (.*)', l.strip())
        if m: add(m[3], m[1], f'memory:{m[2]}', 'memory', 'Master Control' if 'via' not in m[2] else m[2].split('via ')[-1])

profiles = json.load(open(f'{RAW}/agents/profiles.json'))
for f in sorted(glob.glob(f'{RAW}/transcripts/*.txt')):
    bid = os.path.basename(f).split('_')[0]
    bname = next((v['name'] for k, v in profiles.items() if k.startswith(bid)), bid)
    for l in open(f):
        m = re.match(r'- position (\d+) \(([^)]*)\) (.*)', l.strip())
        if m:
            speaker = m[2].split(',')[0]
            add(m[3].strip('… '), 'undated', f'transcript:{bname}#pos{m[1]} ({speaker})', 'transcript', bname)

for f in sorted(glob.glob(f'{RAW}/context_snapshot/*.md')):
    sec = ''
    for l in open(f):
        s = l.rstrip()
        if s.startswith('#'): sec = s.lstrip('# ').replace('*', ''); continue
        if re.match(r'^\s*(-|\d+\.|\|)\s', s) and not re.match(r'^\|\s*-', s):
            dm = re.search(r'(\d{1,2}) Nov', s) or re.search(r'(\d{1,2}) Nov', sec)
            d_ = f'2026-11-{int(dm[1]):02d}' if dm else 'undated'
            add(s.strip(' -|').replace(' | ', ' · '), d_, f'{os.path.basename(f)} › {sec[:60]}', 'context')

# ---------- dedupe ----------
def norm(t): return re.sub(r'[^a-z0-9 ]', '', t.lower())[:220]
uniq = []; seen = {}
for x in facts:
    n = norm(x['text'])
    if n in seen: continue
    dup = False
    for u in uniq[-400:]:
        if abs(len(u['_n']) - len(n)) < 40 and difflib.SequenceMatcher(None, u['_n'], n).quick_ratio() > 0.93 and difflib.SequenceMatcher(None, u['_n'], n).ratio() > 0.9:
            dup = True; break
    if dup: continue
    x['_n'] = n; seen[n] = 1; uniq.append(x)
print('facts', len(facts), 'unique', len(uniq), file=sys.stderr)

# ---------- tagging ----------
TOPICS = {
 'davide-decisions': r'\bDavide\b.*\b(rul|approv|decid|confirm|accept|kill|reject|order|instruct|dropped|set|wants|said|gave|let)',
 'standing-rules': r'\b(never|always|must|only|rule|do not|don\'t|not allowed|banned|no .{0,25} before)\b',
 'team': r'\b(Sterrenberg|Francois|Ian|Hazel|Janae|Eddie|Erich|Michael|Andries|Elmien|Karin|Rozanne|setter|closer|BDR)\b|U0[A-Z0-9]{8,}',
 'lead-handling': r'\b(lead|reply|replied|nurture|outreach|patient|buyer|opt.?out|DND|STOP|reactivat|owner|unowned)',
 'booking-and-calendars': r'\b(book|calendar|walkthrough|webinar|slot|appointment|discovery|round.robin)',
 'targets-kpis': r'\b(target|HQ|KPI|per day|a day|/20|2,000|40 sales|baseline|MTD|gap \d)',
 'products-positioning': r'\b(Optimum|Neuro|panel|pric|R\d[\d,]*|claim|brochure|device|vibration|PBM|red light|SoftWave|booth)',
 'channels': r'\b(WhatsApp|Slack|HighLevel|HL|e-?mail|SMS|template|Meta|channel|Gmail|#\w+)',
 'bots': r'\b(bot|Master Control|Outreach Control|\bOC\b|routine|Smartbot|Sales Desk|Radar|QA)\b',
}
for x in uniq:
    x['tags'] = [t for t, rx in TOPICS.items() if re.search(rx, x['text'], re.I)]
untagged = [x for x in uniq if not x['tags']]
labels = list(TOPICS)
for i in range(0, len(untagged), 8):
    batch = untagged[i:i+8]
    p = ('Classify each numbered fact into ONE topic from: ' + ', '.join(labels) + ', other.\n'
         'Answer only lines like "1: topic".\n\n' + '\n'.join(f'{j+1}: {b["text"][:300]}' for j, b in enumerate(batch)))
    try: out = ollama(p, num_predict=120)
    except Exception as e: out = ''
    for line in out.splitlines():
        m = re.match(r'\s*(\d+)\s*[:.)-]\s*([a-z-]+)', line)
        if m and 0 < int(m[1]) <= len(batch) and m[2] in labels:
            batch[int(m[1])-1]['tags'] = [m[2]]; batch[int(m[1])-1]['tagged_by'] = 'ollama'
for x in uniq:
    if not x['tags']: x['tags'] = ['other']
json.dump([{k: v for k, v in x.items() if k != '_n'} for x in uniq], open(f'{BASE}/raw/facts_tagged.json', 'w'), indent=1)

# ---------- notes ----------
TITLES = {'davide-decisions': "Davide's decisions (rulings log)", 'standing-rules': 'Standing rules', 'team': 'Team: people, roles, Slack IDs, owners',
          'lead-handling': 'Lead handling', 'booking-and-calendars': 'Booking and calendars (closer/sales vs walkthrough webinars)',
          'targets-kpis': 'Targets and KPIs', 'products-positioning': 'Products and positioning', 'channels': 'Channels (WhatsApp, Slack, HighLevel, email)',
          'bots': 'Bots', 'other': 'Other facts'}
RELATED = {'davide-decisions': ['standing-rules', 'decision-model'], 'standing-rules': ['davide-decisions', 'lead-handling', 'channels'],
           'team': ['bots', 'lead-handling'], 'lead-handling': ['booking-and-calendars', 'standing-rules', 'team'],
           'booking-and-calendars': ['lead-handling', 'targets-kpis', 'decision-model'], 'targets-kpis': ['booking-and-calendars', 'team'],
           'products-positioning': ['standing-rules', 'channels'], 'channels': ['standing-rules', 'bots'], 'bots': ['team', 'channels'], 'other': ['index']}
def fm(title, tags, source):
    return f'---\ntitle: "{title}"\ntags: [{", ".join(tags)}]\nsource: "{source}"\ndate: {TODAY}\n---\n\n'
def sort_key(x): return (x['date'] == 'undated', x['date'] if x['date'] != 'undated' else '', x['kind'])
os.makedirs(NOTES, exist_ok=True)
note_counts = {}
for topic in list(TITLES):
    if topic == 'bots': continue
    items = [x for x in uniq if topic in x['tags']]
    if topic == 'davide-decisions':
        items = [x for x in items if x['kind'] != 'transcript' or 'Davide' in x['text']]
    items.sort(key=sort_key, reverse=False)
    note_counts[topic] = len(items)
    comp = headroom_compress([{'d': x['date'], 't': x['text'][:400]} for x in items], topic, f'Summarise the key points about {topic}.')
    ctx = json.dumps(comp)[:9000]
    try:
        summ = ollama(f'You are summarising internal company notes for MedWave (South Africa). Topic: {TITLES[topic]}.\n'
                      f'From the facts below, write 6 short bullet points of the most important durable points. Use only the facts given; no invention.\n\nFACTS:\n{ctx}', num_predict=350)
    except Exception as e: summ = f'(summary failed: {e})'
    body = fm(TITLES[topic], ['medwave', 'brain', topic], 'Master Control memory, bot transcripts (search snippets), /workspace/context docs')
    body += f'# {TITLES[topic]}\n\nRelated: ' + ' · '.join(f'[[{r}]]' for r in RELATED[topic]) + ' · [[index]]\n\n'
    body += f'## Local summary ({MODEL}, unverified — check against facts below)\n\n{redact(summ)}\n\n## Facts ({len(items)}, deduplicated, oldest first)\n\n'
    cur = None
    for x in items:
        if x['date'] != cur:
            cur = x['date']; body += f'\n### {cur}\n\n'
        body += f'- {x["text"]}  \n  _source: {x["source"]}_\n'
    open(f'{NOTES}/{topic}.md', 'w').write(body)

# bots note
lines = []
for bid, v in sorted(profiles.items(), key=lambda kv: kv[1]['name'] or ''):
    desc = redact(v.get('description') or '')
    if desc:
        try: one = ollama(f'In ONE sentence of max 25 words, say what this bot does. No preamble.\n\n{desc[:2500]}', num_predict=60)
        except Exception: one = desc[:200]
    else:
        tr = [x['text'] for x in uniq if x.get('bot') == v['name']][:6]
        one = ollama('In ONE sentence of max 25 words, guess what this bot does from these snippets of its chat. Start with "Likely:".\n\n' + '\n'.join(t[:300] for t in tr), num_predict=60) if tr else '(no profile description and no transcript evidence — OPEN)'
    lines.append(f'- **{v["name"]}** (`{bid}`): {redact(one).splitlines()[0] if one else ""}')
body = fm('Bots', ['medwave', 'brain', 'bots'], 'agent profile.json files + transcript snippets; one-liners by Ollama')
body += '# Bots (31 agents)\n\nRelated: [[team]] · [[channels]] · [[index]]\n\nOne-liners written locally by ' + MODEL + ' from each profile description (or, where a profile is blank, from transcript snippets and marked "Likely").\n\n' + '\n'.join(lines) + '\n'
open(f'{NOTES}/bots.md', 'w').write(body); note_counts['bots'] = len(lines)

json.dump({'stats': STATS, 'note_counts': note_counts, 'facts_total': len(facts), 'facts_unique': len(uniq),
           'untagged_sent_to_ollama': len(untagged)}, open(f'{BASE}/raw/build_stats.json', 'w'), indent=1)
print(json.dumps(note_counts), STATS['ollama_calls'], file=sys.stderr)
