"""BM25 retrieval over vault facts. No embeddings, no network."""

from pathlib import Path

from brain.paths import repo_root
from brain.retrieve import BM25, Document, VaultIndex, blend, cosine


def test_bm25_ranks_the_matching_fact_first():
    docs = [
        Document("Unowned leads go to Erich straight away.", "memory:profile", "team/erich.md", "2026-11-06", "Erich"),
        Document("Owned leads stay with the owner already on the record.", "memory:profile", "team.md", "2026-11-06", "Owners"),
        Document("Elmien is contacted on Slack only.", "memory:profile", "team/elmien.md", "2026-11-05", "Elmien"),
    ]
    hits = BM25(docs).search("unowned leads Erich", k=2)
    assert len(hits) >= 2
    assert "Erich" in hits[0].text
    assert hits[0].source == "memory:profile"
    assert hits[0].score > hits[1].score


def test_blend_keeps_keyword_order_without_embeddings():
    assert blend(2.0, 2.0, 0.0) == 1.0
    mixed = blend(1.0, 2.0, 1.0)
    assert mixed == 0.7 * 0.5 + 0.3 * 1.0
    assert cosine([1.0, 0.0], [1.0, 0.0]) == 1.0
    assert cosine([1.0, 0.0], [0.0, 1.0]) == 0.0


def test_vault_search_finds_elmien_slack_rule():
    vault = repo_root() / "vault"
    index = VaultIndex.load(vault)
    hits = index.search("Elmien Slack only, never WhatsApp", k=5)
    blob = " ".join(hit.text for hit in hits)
    assert "Elmien" in blob
    assert "Slack" in blob
    assert hits[0].source
    assert hits[0].note.endswith(".md")


def test_vault_search_finds_unowned_erich():
    index = VaultIndex.load(repo_root() / "vault")
    hits = index.search("unowned leads default owner Erich", k=5)
    assert any("Erich" in hit.text for hit in hits)
    assert all(hit.note for hit in hits)
