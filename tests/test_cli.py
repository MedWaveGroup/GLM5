"""CLI commands with Ollama mocked out. Rules still answer."""

import json

from brain.cli import main
from brain.report import build_report


class _Down:
    def generate(self, *args, **kwargs):
        return None

    def embed(self, *args, **kwargs):
        return None

    def pick(self, *args, **kwargs):
        return None, None


def test_decide_and_assign_and_report(capsys, monkeypatch):
    monkeypatch.setattr("brain.decide.OllamaPool", lambda *a, **k: _Down())
    monkeypatch.setattr("brain.commands.OllamaPool", lambda *a, **k: _Down())
    monkeypatch.setattr("brain.ask.OllamaPool", lambda *a, **k: _Down())

    assert main(["decide", "unowned lead with no clear owner"]) == 0
    out = capsys.readouterr().out
    assert "Erich" in out
    assert "Paid model needed: no" in out

    assert main(["assign", "turn off the HighLevel workflow"]) == 0
    out = capsys.readouterr().out
    assert "Sterrenberg" in out
    assert "Francois" in out

    assert main(["assign", "book the installation for Friday"]) == 0
    assert "Janae" in capsys.readouterr().out

    assert main(["report", "--hq", "10", "--whatsapps", "1500", "--sales", "1"]) == 0
    report = capsys.readouterr().out
    assert "20" in report and "2000" in report and "2" in report
    assert "behind" in report

    assert main(["triage-lead", json.dumps({
        "owner": None,
        "practice": True,
        "patients_per_month": 180,
        "setting": "medical",
        "country": "ZA",
    })]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["hq"] is True
    assert payload["owner"] == "Erich"
    assert payload["calendar"] == "closer sales calendar"
    assert payload["product"] == "Neuro"


def test_ask_rules_only_returns_facts(capsys, monkeypatch):
    monkeypatch.setattr("brain.ask.OllamaPool", lambda *a, **k: _Down())
    assert main(["ask", "Who gets unowned leads?", "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["route"] == "rule"
    assert payload["escalate_paid"] is False
    assert "Erich" in payload["answer"]
    assert payload["facts"]
    assert payload["facts"][0]["source"]
    assert payload["model"] is None


def test_report_skeleton_without_numbers():
    report = build_report()
    assert [row["target"] for row in report["rows"]] == [20, 2000, 2]
    assert all(row["actual"] is None for row in report["rows"])
    assert report["escalate_paid"] is False


def test_local_model_is_used_when_the_pool_answers(capsys, monkeypatch):
    class _Up(_Down):
        def generate(self, *args, **kwargs):
            return {"text": "Erich, because the rule says so.", "model": "qwen2.5:3b", "host": "linux-box"}

    monkeypatch.setattr("brain.ask.OllamaPool", lambda *a, **k: _Up())
    assert main(["ask", "Who gets unowned leads?"]) == 0
    out = capsys.readouterr().out
    assert "Erich" in out
    assert "qwen2.5:3b" in out
    assert "linux-box" in out
