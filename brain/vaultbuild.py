"""Compile sources/notes into an Obsidian vault with atomic rule and person notes."""

from __future__ import annotations

import json
import re
import shutil
from collections import OrderedDict
from pathlib import Path

from brain.privacy import leaks, redact
from brain.rules import RULES

_CHUNK = 70

_PEOPLE = [
    ("davide-duranti", "Davide Duranti", ["Davide"], "CEO", None,
     "Buyers, Red decisions, and any spend above R5,000 come to him. Bots report to Master Control, not to him."),
    ("ian", "Ian", ["Ian"], "Operations, stock and fulfilment", "U0BFPGTE2D9",
     "Owns stock and fulfilment, and the NRCS/FDA chase. Stuck agreements and missing deposits go to Ian or Francois by direct email."),
    ("francois", "Francois van der Merwe", ["Francois"], "CRO", "U06TXP9D7BR",
     "Manages the setters, events, and webinars. A HighLevel workflow stays on unless he or Sterrenberg confirms."),
    ("sterrenberg", "Sterrenberg", ["Sterrenberg", "Sterrenberg Smit"], "Automations and reactivation", "U09M1N16GCF",
     "Not a BDR. Owns HighLevel automations. Spell the name Sterrenberg even when dictation garbles it."),
    ("erich", "Erich", ["Erich"], "BDR / setter. Default owner for unowned leads", None,
     "Leads with no clear owner go to Erich immediately. Leads that already have an owner stay put."),
    ("eddie", "Eddie", ["Eddie"], "Setter", "U0AEPSHA4FK",
     "Setter under Francois. There is a later note that Sterrenberg said Eddie is not a BDR; reconcile before changing HighLevel ownership."),
    ("hazel", "Hazel", ["Hazel", "Hazel Jennecke"], "Setter", None,
     "Setter under Francois. No confirmed Slack ID in this export."),
    ("michael", "Michael Steytler", ["Michael Steytler", "Michael"], "Setter", None,
     "Setter under Francois."),
    ("andries", "Andries Maritz", ["Andries"], "Closer, Discovery calendar", None,
     "Discovery closer. With Elmien, accountable for Give Give Give Take before and after every sales call."),
    ("elmien", "Elmien Geldenhuys", ["Elmien"], "Closer, Clinical calendar", "U09ML23JRBM",
     "Clinical 1:1 closer. Contact her on Slack only. Never WhatsApp, SMS, or email from the bots."),
    ("karin", "Karin Duranti", ["Karin"], "Referrals", None,
     "Owns referrals, target 2 a day."),
    ("janae", "Janae Vermeulen", ["Janae"], "Installations", None,
     "Owns installations. Daily shape: 2 completed, 2 future installs booked, 2 referrals collected."),
    ("rozanne", "Rozanne Diederichs", ["Rozanne"], "Finance / legal admin", None,
     "Sees the Notion work with Davide, Ian, and Francois. NDAs are chased via Rozanne and Ian."),
    ("anthony", "Anthony Polenski", ["Anthony"], "USA Head of Growth", None,
     "Ruled that US outreach is email only until SMS consent exists. An older contract says Anthony Bowers; reconcile before anything legal."),
]



def _install_objections(out_dir: Path, notes_dir: Path) -> int:
    """Copy sources/objections cards and the objections MOC into the vault."""
    src_dir = Path(notes_dir).parent / "objections"
    moc = Path(notes_dir).parent / "objections.md"
    count = 0
    if src_dir.is_dir():
        dest = Path(out_dir) / "objections"
        dest.mkdir(parents=True, exist_ok=True)
        for path in sorted(src_dir.glob("*.md")):
            text = redact(path.read_text(encoding="utf-8", errors="replace"))
            _write(dest / path.name, text)
            count += 1
    if moc.exists():
        text = redact(moc.read_text(encoding="utf-8", errors="replace"))
        _write(Path(out_dir) / "objections.md", text)
    return count


def compile_vault(notes_dir: Path, decision_model: Path, out_dir: Path) -> dict:
    notes_dir = Path(notes_dir)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    _reset(out_dir)
    _write_obsidian(out_dir)

    written = []
    fact_total = 0
    topic_counts: dict[str, int] = {}

    for path in sorted(notes_dir.glob("*.md")):
        if path.name == "index.md":
            continue
        original = path.read_text(encoding="utf-8", errors="replace")
        text = redact(original)
        topic = path.stem
        if topic == "workspace-index":
            _write(out_dir / "workspace-index.md", text)
            written.append("workspace-index.md")
            topic_counts[topic] = "workspace files"
            continue
        if topic == "bots":
            written.extend(_write_bots(out_dir, text))
            topic_counts["bots"] = text.count("\n- ")
            continue
        meta, body = _frontmatter(text)
        pre, facts = _parse_facts(body, meta.get("date") or "2026-11-09")
        facts = [_redact_fact(fact) for fact in facts]
        topic_counts[topic] = len(facts)
        fact_total += len(facts)
        links = _write_logs(out_dir, topic, meta, facts)
        written.extend(links)
        moc = _moc(topic, meta, pre, links, facts)
        _write(out_dir / f"{topic}.md", moc)
        written.append(f"{topic}.md")

    rule_links = _write_rules(out_dir)
    people_links = _write_people(out_dir, notes_dir)
    product_links = _write_products(out_dir)
    if decision_model.exists():
        model = redact(decision_model.read_text(encoding="utf-8", errors="replace"))
        model = model.replace("[[notes/", "[[")
        model = model.replace("[[../decision-model|decision-model]]", "[[decision-model]]")
        _write(out_dir / "decision-model.md", model)
        written.append("decision-model.md")
    obj_count = _install_objections(out_dir, notes_dir)
    if obj_count:
        topic_counts["objections"] = obj_count
    _write(out_dir / "Start here.md", _start_here(rule_links, people_links, product_links))
    _write(out_dir / "index.md", _index(out_dir, topic_counts))
    problems = _scan(out_dir)
    if problems:
        raise RuntimeError("privacy scan failed: " + "; ".join(problems[:8]))
    return {
        "facts": fact_total,
        "topics": topic_counts,
        "note_files": len(list(out_dir.rglob("*.md"))),
        "rules": len(rule_links),
        "people": len(people_links),
    }


def _reset(out_dir: Path) -> None:
    for child in list(out_dir.iterdir()):
        if child.name == ".obsidian":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        elif child.suffix == ".md":
            child.unlink()


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def _frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    meta = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip().strip('"')
    return meta, text[end + 5 :]


def _parse_facts(body: str, default_date: str) -> tuple[str, list[dict]]:
    if "\n## Facts" in "\n" + body:
        pre, rest = re.split(r"\n## Facts[^\n]*\n", "\n" + body, maxsplit=1)
        pre = pre.lstrip("\n")
        region = rest
    else:
        pre = ""
        region = body
    facts = []
    current_date = default_date
    current = None

    def flush():
        nonlocal current
        if current and current["text"].strip():
            facts.append(current)
        current = None

    for line in region.splitlines():
        if line.startswith("### "):
            flush()
            current_date = line[4:].strip() or default_date
            continue
        if line.startswith("- "):
            flush()
            current = {"date": current_date, "text": line[2:].strip(), "source": ""}
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
    return pre, facts


def _redact_fact(fact: dict) -> dict:
    return {
        "date": fact["date"],
        "text": redact(fact["text"]),
        "source": redact(fact["source"]),
    }


def _write_logs(out_dir: Path, topic: str, meta: dict, facts: list[dict]) -> list[str]:
    grouped: OrderedDict[str, list[dict]] = OrderedDict()
    for fact in facts:
        grouped.setdefault(fact["date"] or "undated", []).append(fact)
    links = []
    title = meta.get("title") or topic
    source = meta.get("source") or "MedWave brain export"
    folder = out_dir / topic
    for date, items in grouped.items():
        chunks = [items[i : i + _CHUNK] for i in range(0, len(items), _CHUNK)] or [[]]
        for index, chunk in enumerate(chunks, start=1):
            suffix = f"-part-{index}" if len(chunks) > 1 else ""
            stem = f"{topic}-{_slug_date(date)}{suffix}"
            rel = f"{topic}/{stem}.md"
            part = f" (part {index})" if len(chunks) > 1 else ""
            lines = [
                "---",
                f'title: "{title} — {date}{part}"',
                f"tags: [medwave, brain, {topic}]",
                f'source: "{_yaml(source)}"',
                f"date: {date if re.match(r'\d{4}-\d{2}-\d{2}', date) else '2026-11-09'}",
                "---",
                "",
                f"# {title} — {date}{part}",
                "",
                f"Part of [[{topic}]]. Index: [[index]]. Start: [[Start here]].",
                "",
            ]
            for fact in chunk:
                lines.append(f"- {fact['text']}  ")
                if fact["source"]:
                    lines.append(f"  _source: {fact['source']}_")
            lines.append("")
            _write(folder / f"{stem}.md", "\n".join(lines))
            links.append(rel[:-3])  # wikilink path without .md
    return links


def _slug_date(date: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", date).strip("-").lower()
    return slug or "undated"


def _moc(topic: str, meta: dict, pre: str, links: list[str], facts: list[dict]) -> str:
    title = meta.get("title") or topic
    source = meta.get("source") or "MedWave brain export"
    cleaned = _clean_preamble(pre)
    lines = [
        "---",
        f'title: "{_yaml(title)}"',
        f"tags: [medwave, brain, {topic}]",
        f'source: "{_yaml(source)}"',
        "date: 2026-11-09",
        "---",
        "",
        f"# {title}",
        "",
        cleaned,
        "",
        f"## Fact log ({len(facts)} facts)",
        "",
    ]
    if topic == "standing-rules":
        lines += ["## Rule cards", ""]
        for rule in RULES:
            lines.append(f"- [[{rule.id}|{rule.title}]]")
        lines.append("")
    if topic == "team":
        lines += ["## People", ""]
        for slug, name, *_rest in _PEOPLE:
            lines.append(f"- [[{slug}|{name}]]")
        lines.append("")
        lines.append(
            "Slack IDs confirmed in the export stay on the person notes. "
            "U093SEARUMC is unresolved (not Hazel). Hazel has no confirmed Slack ID."
        )
        lines.append("")
    if topic == "products-positioning":
        lines += [
            "## Products",
            "",
            "- [[optimum|Optimum]] — aesthetics only",
            "- [[neuro|Neuro]] — medical settings",
            "",
        ]
    lines.append("## Dated notes")
    lines.append("")
    for link in links:
        label = link.split("/")[-1].replace(topic + "-", "").replace("-", " ")
        lines.append(f"- [[{link}|{label}]]")
    lines += ["", "Related: [[index]] · [[Start here]] · [[decision-model]]", ""]
    return "\n".join(lines)


def _clean_preamble(pre: str) -> str:
    if "<<ccr:" in pre:
        pre = re.sub(
            r"## Local summary[^\n]*\n.*?(?=\n## |\Z)",
            "## Local summary\n\n_Omitted. The export summary was a Headroom compression artefact. Use the fact log._\n",
            pre,
            count=1,
            flags=re.S,
        )
    kept = []
    for line in pre.splitlines():
        if "<<ccr:" in line or line.startswith("# "):
            continue
        kept.append(line)
    text = "\n".join(kept).strip()
    if "Local summary" in text:
        text = (
            "> Unverified local summary. A rule card or [[decision-model]] wins if they disagree.\n\n"
            + text
        )
    return text


def _write_rules(out_dir: Path) -> list[str]:
    links = []
    folder = out_dir / "standing-rules"
    for rule in RULES:
        body = "\n".join([
            "---",
            f'title: "{_yaml(rule.title)}"',
            "tags: [medwave, brain, standing-rules, rule]",
            'source: "decision-model.md"',
            "date: 2026-11-09",
            "---",
            "",
            f"# {rule.title}",
            "",
            rule.ruling,
            "",
            f"Cite: {rule.citation}",
            "",
            "Related: [[standing-rules]] · [[decision-model]] · [[index]] · [[Start here]]",
            "",
        ])
        _write(folder / f"{rule.id}.md", body)
        links.append(rule.id)
    return links


def _write_people(out_dir: Path, notes_dir: Path) -> list[str]:
    team_path = notes_dir / "team.md"
    facts = []
    if team_path.exists():
        text = redact(team_path.read_text(encoding="utf-8", errors="replace"))
        _pre, facts = _parse_facts(_frontmatter(text)[1], "2026-11-09")
    links = []
    folder = out_dir / "team"
    for slug, name, aliases, role, slack, blurb in _PEOPLE:
        samples = _exemplars(facts, aliases)
        slack_line = f"Slack: `{slack}`." if slack else "Slack ID: not confirmed in this export."
        lines = [
            "---",
            f'title: "{name}"',
            "tags: [medwave, brain, team, person]",
            'source: "notes/team.md"',
            "date: 2026-11-09",
            f"aliases: [{name}]",
            "---",
            "",
            f"# {name}",
            "",
            f"Role: {role}.",
            "",
            slack_line,
            "",
            blurb,
            "",
            "Related: [[team]] · [[standing-rules]] · [[index]] · [[Start here]]",
            "",
        ]
        if slug == "erich":
            lines += [
                "Open: Slack ID U093SEARUMC was seen near Erich and Hazel. The journal says that ID is not Hazel. Do not treat it as confirmed for Erich.",
                "",
            ]
        if samples:
            lines.append("## From the team log")
            lines.append("")
            for fact in samples:
                lines.append(f"- ({fact['date']}) {fact['text']}  ")
                if fact["source"]:
                    lines.append(f"  _source: {fact['source']}_")
            lines.append("")
        _write(folder / f"{slug}.md", "\n".join(lines))
        links.append(slug)
    return links


def _exemplars(facts: list[dict], aliases: list[str], limit: int = 5) -> list[dict]:
    scored = []
    for fact in facts:
        if not any(re.search(rf"\b{re.escape(alias)}\b", fact["text"]) for alias in aliases):
            continue
        score = 0
        if re.search(r"owner|Slack|BDR|closer|setter|role", fact["text"], re.I):
            score += 3
        score -= min(len(fact["text"]), 800) / 800
        scored.append((score, fact))
    scored.sort(key=lambda item: item[0], reverse=True)
    chosen = []
    seen = set()
    for _score, fact in scored:
        key = fact["text"][:120]
        if key in seen:
            continue
        seen.add(key)
        chosen.append(fact)
        if len(chosen) >= limit:
            break
    return chosen


def _write_products(out_dir: Path) -> list[str]:
    folder = out_dir / "products-positioning"
    optimum = "\n".join([
        "---",
        'title: "Optimum"',
        "tags: [medwave, brain, products-positioning]",
        'source: "decision-model.md"',
        "date: 2026-11-09",
        "---",
        "",
        "# Optimum",
        "",
        "Offer the Optimum panel only in aesthetics settings: spas and aesthetic or skin practices.",
        "",
        "Cite: Davide, 7 Nov 2026. See [[decision-model]] and [[optimum-neuro]].",
        "",
        "Related: [[products-positioning]] · [[neuro]] · [[standing-rules]]",
        "",
    ])
    neuro = "\n".join([
        "---",
        'title: "Neuro"',
        "tags: [medwave, brain, products-positioning]",
        'source: "decision-model.md"',
        "date: 2026-11-09",
        "---",
        "",
        "# Neuro",
        "",
        "Offer the Neuro panel (Neuro100S) in medical settings.",
        "",
        'Killed claims: "9 in 10 sales are Neuro-100S" and "best seller" (Davide, 2 Nov 2026).',
        "",
        "Cite: Davide, 7 Nov 2026. See [[decision-model]] and [[optimum-neuro]].",
        "",
        "Related: [[products-positioning]] · [[optimum]] · [[standing-rules]]",
        "",
    ])
    _write(folder / "optimum.md", optimum)
    _write(folder / "neuro.md", neuro)
    return ["optimum", "neuro"]


def _write_bots(out_dir: Path, text: str) -> list[str]:
    written = []
    folder = out_dir / "bots"
    cards = []
    for line in text.splitlines():
        match = re.match(r"^- \*\*(.+?)\*\* \(`([^`]+)`\):\s*(.*)$", line.strip())
        if not match:
            continue
        name, bot_id, blurb = match.group(1), match.group(2), match.group(3).strip()
        slug = _slug(name)
        body = "\n".join([
            "---",
            f'title: "{_yaml(name)}"',
            "tags: [medwave, brain, bots]",
            'source: "notes/bots.md"',
            "date: 2026-11-09",
            "---",
            "",
            f"# {name}",
            "",
            f"Id: `{bot_id}`.",
            "",
            redact(blurb),
            "",
            "Related: [[bots]] · [[team]] · [[index]] · [[Start here]]",
            "",
        ])
        _write(folder / f"{slug}.md", body)
        cards.append((slug, name, bot_id))
        written.append(f"bots/{slug}.md")
    lines = [
        "---",
        'title: "Bots"',
        "tags: [medwave, brain, bots]",
        'source: "notes/bots.md"',
        "date: 2026-11-09",
        "---",
        "",
        "# Bots",
        "",
        "31 agents. One-liners were written locally when the export was built. Each bot has its own note.",
        "",
        "Related: [[team]] · [[channels]] · [[index]] · [[Start here]]",
        "",
    ]
    for slug, name, bot_id in cards:
        lines.append(f"- [[{slug}|{name}]] (`{bot_id}`)")
    lines.append("")
    _write(out_dir / "bots.md", "\n".join(lines))
    written.append("bots.md")
    return written


def _start_here(rules: list[str], people: list[str], products: list[str]) -> str:
    return "\n".join([
        "---",
        'title: "Start here"',
        "tags: [medwave, brain, moc]",
        'source: "vault compile"',
        "date: 2026-11-09",
        "---",
        "",
        "# Start here",
        "",
        "This is the MedWave manager brain for Master Control. Answer from a rule or from this vault before any paid model is called.",
        "",
        "## Order",
        "",
        "1. A deterministic rule or a lookup in [[standing-rules]] and [[decision-model]].",
        "2. A local Ollama model on loopback (`brain ask`, `brain decide`). Davide's Mac uses `qwen2.5:7b`. The Linux box uses `qwen2.5:3b`.",
        "3. The `escalate_paid` flag, with a reason. A human flag means Davide, not a bigger model.",
        "",
        "## Map",
        "",
        "- [[index]] — every note",
        "- [[decision-model]] — how Davide decides, and the HQ rubric",
        "- [[standing-rules]] — rule cards and the fact log",
        "- [[team]] — one note per person",
        "- [[lead-handling]] · [[objections]] · [[booking-and-calendars]] · [[targets-kpis]]",
        "- [[products-positioning]] · [[channels]] · [[bots]] · [[davide-decisions]]",
        "- [[other]] · [[workspace-index]]",
        "",
        "## Commands",
        "",
        "- `brain ask \"question\"`",
        "- `brain decide \"situation\"`",
        "- `brain triage-lead '{...}'`",
        "- `brain assign \"task\"`",
        "- `brain report`",
        "- `brain ingest`",
        "- `/workspace/team/outreach-control/ask_brain.sh \"question\"` — objection notes only, then qwen2.5:3b",
        "",
        "Local first, tokens last.",
        "",
    ])


def _index(out_dir: Path, topic_counts: dict[str, int]) -> str:
    lines = [
        "---",
        'title: "MedWave brain index"',
        "tags: [medwave, brain, index]",
        'source: "vault compile"',
        "date: 2026-11-09",
        "---",
        "",
        "# MedWave brain index",
        "",
        "Built from the 9 Nov 2026 export. Facts stay dated and sourced. Start at [[Start here]].",
        "",
        "## Topics",
        "",
    ]
    for topic, count in topic_counts.items():
        label = f"{count} items" if isinstance(count, int) else str(count)
        lines.append(f"- [[{topic}]] ({label})")
    lines += [
        "- [[decision-model]] — how Davide decides, plus the HQ rubric",
        "- [[Start here]]",
        "",
        "## How to use",
        "",
        "- Rulings with dates: [[davide-decisions]]. Hard rules: [[standing-rules]]. Objection cards: [[objections]].",
        "- Booking a lead: [[booking-and-calendars]], then the HQ rubric in [[decision-model]].",
        "- Who is who: [[team]] and [[bots]].",
        "- Each fact carries a `_source_` line. Transcript snippets are undated search excerpts.",
        "",
        "## All notes",
        "",
    ]
    for path in sorted(out_dir.rglob("*.md")):
        if path.name == "index.md":
            continue
        rel = path.relative_to(out_dir).as_posix()[:-3]
        lines.append(f"- [[{rel}]]")
    lines.append("")
    return "\n".join(lines)


def _write_obsidian(out_dir: Path) -> None:
    folder = out_dir / ".obsidian"
    folder.mkdir(parents=True, exist_ok=True)
    app = {
        "legacyEditor": False,
        "livePreview": True,
        "showLineNumber": False,
        "strictLineBreaks": False,
        "useMarkdownLinks": False,
        "newFileLocation": "folder",
        "attachmentFolderPath": "attachments",
        "alwaysUpdateLinks": True,
    }
    appearance = {"baseFontSize": 16, "theme": "system"}
    core = {
        "file-explorer": True,
        "global-search": True,
        "switcher": True,
        "graph": True,
        "backlink": True,
        "outgoing-link": True,
        "tag-pane": True,
        "page-preview": True,
        "note-composer": True,
        "command-palette": True,
        "editor-status": True,
        "outline": True,
        "word-count": True,
        "file-recovery": True,
    }
    graph = {"collapse-filter": True, "showTags": False, "showAttachments": False}
    (folder / "app.json").write_text(json.dumps(app, indent=2) + "\n", encoding="utf-8")
    (folder / "appearance.json").write_text(json.dumps(appearance, indent=2) + "\n", encoding="utf-8")
    (folder / "core-plugins.json").write_text(json.dumps(core, indent=2) + "\n", encoding="utf-8")
    (folder / "community-plugins.json").write_text("[]\n", encoding="utf-8")
    (folder / "graph.json").write_text(json.dumps(graph, indent=2) + "\n", encoding="utf-8")


def _scan(out_dir: Path) -> list[str]:
    problems = []
    for path in out_dir.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".md", ".json"}:
            continue
        found = leaks(path.read_text(encoding="utf-8", errors="replace"))
        if found:
            problems.append(f"{path.name}: {', '.join(found)}")
    return problems


def _yaml(value: str) -> str:
    return value.replace('"', "'")


def _slug(name: str) -> str:
    slug = name.lower().replace("·", " ")
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug or "note"
