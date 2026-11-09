"""The committed vault keeps every source fact and the Obsidian entry points."""

from pathlib import Path

from brain.paths import repo_root
from brain.privacy import leaks
from brain.vaultbuild import _frontmatter, _parse_facts, compile_vault


def test_entry_points_exist():
    vault = repo_root() / "vault"
    assert (vault / "Start here.md").exists()
    assert (vault / "index.md").exists()
    assert (vault / "decision-model.md").exists()
    assert (vault / ".obsidian" / "app.json").exists()
    assert (vault / ".obsidian" / "core-plugins.json").exists()
    assert (vault / "standing-rules" / "unowned-leads-erich.md").exists()
    assert (vault / "standing-rules" / "elmien-slack-only.md").exists()
    assert (vault / "team" / "erich.md").exists()
    assert (vault / "team" / "elmien.md").exists()
    assert (vault / "products-positioning" / "optimum.md").exists()
    assert (vault / "products-positioning" / "neuro.md").exists()
    assert any((vault / "bots").glob("*.md"))
    start = (vault / "Start here.md").read_text(encoding="utf-8")
    assert "[[standing-rules]]" in start
    assert "[[index]]" in start
    assert "local first" in start.lower() or "Local first" in start


def test_source_facts_are_in_the_vault():
    root = repo_root()
    vault_text = "\n".join(
        path.read_text(encoding="utf-8", errors="replace")
        for path in (root / "vault").rglob("*.md")
    )
    missing = []
    for path in sorted((root / "sources" / "notes").glob("*.md")):
        if path.name in {"index.md", "bots.md", "workspace-index.md"}:
            continue
        meta, body = _frontmatter(path.read_text(encoding="utf-8"))
        _pre, facts = _parse_facts(body, meta.get("date") or "2026-11-09")
        for fact in facts:
            snippet = fact["text"][:100]
            if snippet not in vault_text:
                missing.append(f"{path.name}: {snippet}")
    assert not missing, "\n".join(missing[:8])


def test_compile_round_trip(tmp_path):
    notes = tmp_path / "notes"
    notes.mkdir()
    (notes / "standing-rules.md").write_text(
        "---\ntitle: \"Standing rules\"\ntags: [medwave]\nsource: \"test\"\ndate: 2026-11-09\n---\n\n"
        "# Standing rules\n\nRelated: [[index]]\n\n## Facts (1)\n\n"
        "### 2026-11-06\n\n"
        "- Unowned leads go to Erich.\n  _source: memory:profile_\n",
        encoding="utf-8",
    )
    model = tmp_path / "decision-model.md"
    model.write_text("# How Davide decides\n\nRelated: [[notes/standing-rules]]\n", encoding="utf-8")
    out = tmp_path / "vault"
    stats = compile_vault(notes, model, out)
    assert stats["facts"] == 1
    assert (out / "Start here.md").exists()
    assert (out / ".obsidian" / "app.json").exists()
    assert (out / "standing-rules" / "unowned-leads-erich.md").exists()
    log = next((out / "standing-rules").glob("standing-rules-2026-11-06.md"))
    assert "Unowned leads go to Erich." in log.read_text(encoding="utf-8")
    assert "[[standing-rules]]" in (out / "decision-model.md").read_text(encoding="utf-8")
    assert leaks(log.read_text(encoding="utf-8")) == []


def test_published_tree_has_no_emails_phones_or_secrets():
    root = repo_root()
    skip = {".git", ".venv", "venv", "__pycache__", ".pytest_cache"}
    problems = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in skip for part in path.parts):
            continue
        if path.suffix.lower() not in {".md", ".json", ".toml", ".txt"}:
            continue
        found = leaks(path.read_text(encoding="utf-8", errors="replace"))
        if found:
            problems.append(f"{path.relative_to(root)}: {', '.join(found)}")
    assert not problems, "\n".join(problems[:12])
