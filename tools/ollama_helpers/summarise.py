"""Local summariser: scrub -> chunk -> Ollama bullets -> scrub again.
Used for KB sections, pre-call thread summaries, Slack digests and report drafts.
Never reads brain-export/raw/ or context/confidential/.

  python3 summarise.py FILE [FILE...] --bullets 8 --focus "contact rules"
"""
from __future__ import annotations
import argparse, os, sys

import ollama_local
from privacy_scrub import scrub

FORBIDDEN = ("/brain-export/raw", "/context/confidential")
CHUNK = 6000


def _chunks(text: str, n: int = CHUNK):
    paras, buf = text.split("\n\n"), ""
    for p in paras:
        if len(buf) + len(p) > n and buf:
            yield buf
            buf = ""
        buf += p + "\n\n"
    if buf.strip():
        yield buf


def summarise(text: str, bullets: int = 8, focus: str = "") -> str | None:
    text = scrub(text)
    sys_p = ("You condense internal operating notes for MedWave's CEO. Write plain, short bullet "
             "points starting with '- '. Keep rules exact (numbers, times, names of roles). "
             "No phone numbers, emails, tokens or customer names. No preamble.")
    parts = []
    for c in _chunks(text):
        out = ollama_local.generate(
            f"Focus: {focus or 'the rules and process'}. Give at most {bullets} bullets.\n\n{c}",
            system=sys_p, step="summarise_chunk", num_predict=450)
        if out is None:
            return None
        parts.append(out)
    if len(parts) > 1:
        out = ollama_local.generate(
            f"Merge and dedupe into at most {bullets} bullets:\n\n" + "\n".join(parts),
            system=sys_p, step="summarise_merge", num_predict=450)
        parts = [out or "\n".join(parts)]
    return scrub(parts[0])


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--bullets", type=int, default=8)
    ap.add_argument("--focus", default="")
    ap.add_argument("--max-chars", type=int, default=18000)
    a = ap.parse_args()
    txt = ""
    for f in a.files:
        if any(x in os.path.abspath(f) for x in FORBIDDEN):
            sys.exit(f"refusing restricted path: {f}")
        txt += open(f).read()[: a.max_chars] + "\n\n"
    res = summarise(txt, a.bullets, a.focus)
    if res is None:
        print("escalate_paid: Ollama unavailable", file=sys.stderr)
        sys.exit(2)
    print(res)
