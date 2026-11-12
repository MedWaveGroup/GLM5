"""Repeated-wording check: is a draft too close to anything this contact already got?

Step 1 (deterministic): word-shingle Jaccard + difflib ratio.
Step 2 (Ollama, only in the grey band): ask the local model whether two texts say
the same thing. No paid model. Usage:
  python3 dedupe_wording.py --draft "text" --prior "old 1" --prior "old 2" [--no-ollama]
"""
from __future__ import annotations
import argparse, difflib, json, re

HARD, GREY = 0.80, 0.55


def _norm(t: str) -> str:
    t = re.sub(r"\{\{?\w+\}?\}|\bhi\s+\w+[,!]?", " ", t.lower())  # drop names/vars
    return re.sub(r"[^a-z0-9 ]+", " ", t)


def _shingles(t: str, n: int = 3) -> set:
    w = _norm(t).split()
    return {tuple(w[i:i + n]) for i in range(max(1, len(w) - n + 1))}


def similarity(a: str, b: str) -> float:
    sa, sb = _shingles(a), _shingles(b)
    jac = len(sa & sb) / max(1, len(sa | sb))
    seq = difflib.SequenceMatcher(None, _norm(a), _norm(b)).ratio()
    return round(max(jac, seq), 3)


def ollama_same(a: str, b: str) -> bool | None:
    try:
        import ollama_local
    except ImportError:
        return None
    out = ollama_local.generate(
        f"Message A:\n{a}\n\nMessage B:\n{b}\n\nWould a reader feel B repeats A "
        "(same opener, same offer, same ask)? Answer JSON {\"same\": true|false}.",
        step="dedupe_grey", json_mode=True, num_predict=20)
    try:
        return bool(json.loads(out)["same"]) if out else None
    except Exception:
        return None


def check(draft: str, priors: list[str], use_ollama: bool = True) -> dict:
    worst, worst_txt = 0.0, ""
    for p in priors:
        s = similarity(draft, p)
        if s > worst:
            worst, worst_txt = s, p
    verdict, engine = "ok", "deterministic"
    if worst >= HARD:
        verdict = "repeat"
    elif worst >= GREY and use_ollama:
        same = ollama_same(draft, worst_txt)
        engine = "ollama" if same is not None else "deterministic"
        verdict = "repeat" if same else ("ok" if same is False else "review")
    elif worst >= GREY:
        verdict = "review"
    return {"verdict": verdict, "max_similarity": worst, "engine": engine}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", required=True)
    ap.add_argument("--prior", action="append", default=[])
    ap.add_argument("--no-ollama", action="store_true")
    a = ap.parse_args()
    print(json.dumps(check(a.draft, a.prior, not a.no_ollama)))
