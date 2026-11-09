"""BM25 retrieval over the vault. Optional Ollama embeddings rerank the top hits."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from pathlib import Path

_WORD = re.compile(r"[a-z0-9]+")
_STOP = {
    "the", "a", "an", "of", "to", "and", "or", "for", "in", "on", "is", "are",
    "with", "that", "this", "be", "as", "at", "by", "from", "it", "its",
}


def tokenize(text: str) -> list[str]:
    return [tok for tok in _WORD.findall(text.lower()) if tok not in _STOP and len(tok) > 1]


@dataclass
class Document:
    text: str
    source: str
    note: str
    date: str
    title: str


@dataclass
class Hit:
    text: str
    source: str
    note: str
    date: str
    title: str
    score: float

    def as_dict(self) -> dict:
        return {
            "text": self.text,
            "source": self.source,
            "note": self.note,
            "date": self.date,
            "title": self.title,
            "score": round(self.score, 4),
        }


def _split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    meta = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta, text[end + 5 :]


def documents_from_markdown(path: Path, vault: Path) -> list[Document]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    meta, body = _split_frontmatter(raw)
    title = meta.get("title") or path.stem
    note = path.relative_to(vault).as_posix()
    date = meta.get("date") or ""
    docs: list[Document] = []
    # The opening paragraph (rule statement or role) is its own document.
    paragraph = []
    for line in body.splitlines():
        if line.startswith("#") or line.startswith("- ") or line.strip() == "":
            if paragraph:
                break
            if line.startswith("#"):
                continue
            continue
        paragraph.append(line.strip())
    if paragraph:
        docs.append(
            Document(
                text=" ".join(paragraph)[:1200],
                source=meta.get("source") or note,
                note=note,
                date=date,
                title=title,
            )
        )
    current_date = date
    current: dict | None = None

    def flush():
        nonlocal current
        if current and current["text"].strip():
            docs.append(
                Document(
                    text=current["text"].strip()[:2000],
                    source=current["source"] or note,
                    note=note,
                    date=current["date"] or date,
                    title=title,
                )
            )
        current = None

    for line in body.splitlines():
        if line.startswith("### "):
            flush()
            current_date = line[4:].strip()
            continue
        if line.startswith("- "):
            flush()
            body_text = line[2:].strip()
            # Index bullets are navigation, not facts.
            if body_text.startswith("[[") or body_text.startswith("|"):
                continue
            current = {"text": body_text, "source": "", "date": current_date}
            continue
        if current is None:
            continue
        stripped = line.strip()
        source = re.match(r"_source:\s*(.+)_?\s*$", stripped)
        if source and stripped.startswith("_source:"):
            current["source"] = source.group(1).rstrip("_").strip()
        elif stripped:
            current["text"] += " " + stripped
    flush()
    # Drop duplicates inside one note.
    seen = set()
    unique = []
    for doc in docs:
        key = re.sub(r"\s+", " ", doc.text.lower())[:240]
        if key in seen:
            continue
        seen.add(key)
        unique.append(doc)
    return unique


def load_documents(vault: Path) -> list[Document]:
    docs = []
    if not vault.exists():
        return docs
    for path in sorted(vault.rglob("*.md")):
        if any(part.startswith(".") for part in path.relative_to(vault).parts):
            continue
        docs.extend(documents_from_markdown(path, vault))
    return docs


class BM25:
    def __init__(self, docs: list[Document], k1: float = 1.5, b: float = 0.75):
        self.docs = docs
        self.k1 = k1
        self.b = b
        self.tokens = [tokenize(doc.text) for doc in docs]
        self.df: dict[str, int] = {}
        for toks in self.tokens:
            for tok in set(toks):
                self.df[tok] = self.df.get(tok, 0) + 1
        self.avg = (sum(len(toks) for toks in self.tokens) / len(self.tokens)) if self.tokens else 0.0
        self.n = len(docs)

    def search(self, query: str, k: int = 8) -> list[Hit]:
        q = tokenize(query)
        if not q or not self.docs:
            return []
        scores = []
        for index, toks in enumerate(self.tokens):
            if not toks:
                continue
            tf: dict[str, int] = {}
            for tok in toks:
                tf[tok] = tf.get(tok, 0) + 1
            score = 0.0
            dl = len(toks)
            for term in q:
                freq = tf.get(term, 0)
                if not freq:
                    continue
                n_q = self.df.get(term, 0)
                idf = math.log(1 + (self.n - n_q + 0.5) / (n_q + 0.5))
                denom = freq + self.k1 * (1 - self.b + self.b * dl / (self.avg or 1))
                score += idf * (freq * (self.k1 + 1)) / denom
            if score > 0:
                scores.append((score, index))
        scores.sort(key=lambda item: item[0], reverse=True)
        hits = []
        seen = set()
        for score, index in scores:
            doc = self.docs[index]
            key = re.sub(r"\s+", " ", doc.text.lower())[:180]
            if key in seen:
                continue
            seen.add(key)
            hits.append(
                Hit(doc.text, doc.source, doc.note, doc.date, doc.title, score)
            )
            if len(hits) >= k:
                break
        return hits


def cosine(a: list[float], b: list[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def blend(bm25_score: float, bm25_max: float, similarity: float) -> float:
    """0.7 keyword, 0.3 local embedding. Similarity is ignored when it is 0."""
    norm = bm25_score / bm25_max if bm25_max else 0.0
    if similarity <= 0:
        return norm
    return 0.7 * norm + 0.3 * similarity


@dataclass
class VaultIndex:
    vault: Path
    bm25: BM25
    docs: list[Document] = field(default_factory=list)

    @classmethod
    def load(cls, vault: Path) -> "VaultIndex":
        docs = load_documents(vault)
        return cls(vault=vault, bm25=BM25(docs), docs=docs)

    def search(self, query: str, k: int = 8, pool=None) -> list[Hit]:
        hits = self.bm25.search(query, k=max(k, 15))
        if not hits:
            return []
        if pool is None:
            return hits[:k]
        try:
            query_vec = pool.embed(query)
        except Exception:
            query_vec = None
        if not query_vec:
            return hits[:k]
        rescored = []
        top = hits[:15]
        maximum = top[0].score or 1.0
        for hit in top:
            try:
                vec = pool.embed(hit.text[:500])
            except Exception:
                vec = None
            sim = cosine(query_vec, vec) if vec else 0.0
            rescored.append((blend(hit.score, maximum, sim), hit, sim))
        # Only reorder when at least one embedding came back.
        if not any(sim > 0 for _, _, sim in rescored):
            return hits[:k]
        rescored.sort(key=lambda item: item[0], reverse=True)
        ordered = []
        for score, hit, _sim in rescored:
            ordered.append(
                Hit(hit.text, hit.source, hit.note, hit.date, hit.title, score)
            )
        return ordered[:k]
