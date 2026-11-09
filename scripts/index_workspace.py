#!/usr/bin/env python3
"""Index /workspace working files locally (inventory + Ollama one-liners for key .md files). No cloud tokens."""
import os, json, time, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from datetime import datetime, date
import urllib.request
BASE=os.environ.get('BRAIN_EXPORT', '/workspace/brain-export'); W=os.environ.get('WORKSPACE_ROOT', '/workspace'); MODEL=os.environ.get('OLLAMA_MODEL','qwen2.5:3b')
SKIP={'brain-export','wenv','wenv-whisper','agent-tools','uploads','node_modules','tmp','artifact','b64','.git'}
PRIORITY=['engine-room','reports','team','strategy','sales','leads-outreach','outreach','people','context','internal','legal','finance','handoffs','briefs','offers','partners','meta_guides','mentor','onboarding','sales-radar','radar','qa','audits','referral','cold-leads','buyers','proposals','tracker']
CAP=int(os.environ.get('CAP','120'))
def redact(t):
    t=re.sub(r'[\w.+-]+@[\w-]+\.[\w.-]+','[email]',t); return re.sub(r'(?<![\w.])\+?\d[\d\s()-]{8,}\d(?![\w.])','[phone]',t)
def ollama(p):
    body={'model':MODEL,'prompt':p,'stream':False,'options':{'temperature':0.1,'num_predict':50,'num_ctx':2048}}
    r=urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:11434/api/generate',data=json.dumps(body).encode(),headers={'Content-Type':'application/json'}),timeout=300)
    return json.load(r)['response'].strip()
inv={}; mds=[]
for root,dirs,files in os.walk(W):
    rel=os.path.relpath(root,W); top=rel.split('/')[0]
    dirs[:]=[d for d in dirs if d not in SKIP and not d.startswith('tmp_')]
    if top in SKIP: continue
    for f in files:
        p=os.path.join(root,f)
        try: st=os.stat(p)
        except OSError: continue
        k=top if rel!='.' else '(root)'
        e=inv.setdefault(k,{'files':0,'bytes':0,'exts':{}}); e['files']+=1; e['bytes']+=st.st_size
        ext=os.path.splitext(f)[1].lower() or '(none)'; e['exts'][ext]=e['exts'].get(ext,0)+1
        if f.endswith('.md') and top in PRIORITY and st.st_size<60000: mds.append((PRIORITY.index(top),-st.st_mtime,p))
json.dump(inv,open(f'{BASE}/raw/workspace_inventory.json','w'),indent=1)
mds.sort(); chosen=mds[:CAP]; rows=[]; calls=0; t0=time.time()
for _,mt,p in chosen:
    txt=open(p,errors='ignore').read()[:1500]
    try: s=ollama('In ONE line (max 20 words) say what this MedWave working file is about. No preamble.\n\nFILE '+os.path.relpath(p,W)+':\n'+txt); calls+=1
    except Exception as ex: s='(summary failed)'
    rows.append((os.path.relpath(p,W),datetime.fromtimestamp(-mt).strftime('%Y-%m-%d'),redact(s.splitlines()[0] if s else '')))
out=f'---\ntitle: "Workspace index"\ntags: [medwave, brain, workspace-index]\nsource: "/workspace file walk + {MODEL} one-liners"\ndate: {date.today()}\n---\n\n# Workspace index\n\nRelated: [[index]] · [[bots]]\n\nIndexed locally; nothing here was read by the cloud model. {sum(v["files"] for v in inv.values())} files across {len(inv)} top-level folders; {len(mds)} candidate .md files, {len(rows)} summarised by {MODEL}.\n\n## Folders\n\n| folder | files | MB | main types |\n|---|---|---|---|\n'
for k,v in sorted(inv.items(),key=lambda kv:-kv[1]['files']):
    ex=', '.join(f'{a} {b}' for a,b in sorted(v['exts'].items(),key=lambda e:-e[1])[:4]); out+=f'| {k} | {v["files"]} | {v["bytes"]/1e6:.1f} | {ex} |\n'
out+='\n## Key working files (one-line local summaries, unverified)\n\n'
cur=None
for path,d,s in rows:
    top=path.split('/')[0]
    if top!=cur: cur=top; out+=f'\n### {top}\n\n'
    out+=f'- `{path}` ({d}): {s}\n'
open(f'{BASE}/notes/workspace-index.md','w').write(out)
json.dump({'ollama_calls':calls,'seconds':round(time.time()-t0),'md_candidates':len(mds),'summarised':len(rows)},open(f'{BASE}/raw/workspace_index_stats.json','w'))
print('done',calls,file=sys.stderr)
