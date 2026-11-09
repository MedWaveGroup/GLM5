"""Host fallback, rules-only mode, and Headroom degrading when it is absent."""

import urllib.error

from brain.config import ConfigError, Host, Settings
from brain.headroom_util import compress_context
from brain.ollama_client import OllamaPool
from brain.decide import decide
from brain.commands import assign


def _settings():
    return Settings(
        hosts=(
            Host("davide-mac", "http://127.0.0.1:11434", "qwen2.5:7b", "M3, 24 GB"),
            Host("linux-box", "http://127.0.0.1:11435", "qwen2.5:3b", "Linux box"),
        ),
        health_timeout_s=0.2,
        generate_timeout_s=0.2,
    )


def test_first_host_down_falls_back_to_second():
    def transport(method, url, body, timeout):
        if "11434" in url:
            raise urllib.error.URLError("connection refused")
        if url.endswith("/api/tags"):
            return {"models": [{"name": "qwen2.5:3b"}]}
        if url.endswith("/api/generate"):
            return {"response": "Use the standing rule."}
        raise AssertionError(url)

    pool = OllamaPool(_settings(), transport)
    host, model = pool.pick()
    assert host.name == "linux-box"
    assert model == "qwen2.5:3b"
    generated = pool.generate("hello")
    assert generated["host"] == "linux-box"
    assert generated["text"] == "Use the standing rule."


def test_mac_profile_wins_when_7b_is_installed():
    def transport(method, url, body, timeout):
        if url.endswith("/api/tags"):
            return {"models": [{"name": "qwen2.5:7b"}, {"name": "qwen2.5:3b"}]}
        raise AssertionError("generate should not be required for pick")

    pool = OllamaPool(_settings(), transport)
    host, model = pool.pick()
    assert host.name == "davide-mac"
    assert model == "qwen2.5:7b"


def test_same_loopback_falls_through_when_only_3b_is_installed():
    """Both profiles use 127.0.0.1:11434. Linux is chosen when 7b is absent."""

    def transport(method, url, body, timeout):
        if url.endswith("/api/tags"):
            return {"models": [{"name": "qwen2.5:3b:latest"}]}
        return {"response": "ok"}

    settings = Settings(
        hosts=(
            Host("davide-mac", "http://127.0.0.1:11434", "qwen2.5:7b"),
            Host("linux-box", "http://127.0.0.1:11434", "qwen2.5:3b"),
        )
    )
    pool = OllamaPool(settings, transport)
    host, model = pool.pick()
    assert host.name == "linux-box"
    assert model.startswith("qwen2.5:3b")


def test_remote_host_is_refused():
    settings = Settings(hosts=(Host("tunnel", "http://example.com:11434", "qwen2.5:3b"),))
    try:
        OllamaPool(settings, lambda *a, **k: {})
    except ConfigError:
        return
    raise AssertionError("non-loopback host should be refused")


def test_generate_falls_back_when_the_first_host_errors():
    calls = []

    def transport(method, url, body, timeout):
        calls.append(url)
        if "11434" in url and url.endswith("/api/generate"):
            raise urllib.error.URLError("reset")
        if url.endswith("/api/tags"):
            return {"models": [{"name": "qwen2.5:7b"}, {"name": "qwen2.5:3b"}]}
        if url.endswith("/api/generate"):
            return {"response": "from the linux box"}
        raise AssertionError(url)

    pool = OllamaPool(_settings(), transport)
    generated = pool.generate("situation")
    assert generated["text"] == "from the linux box"
    assert generated["host"] == "linux-box"
    assert any("11434" in url and url.endswith("/api/generate") for url in calls)


def test_decide_is_rules_only_when_ollama_is_down():
    def transport(method, url, body, timeout):
        raise urllib.error.URLError("down")

    pool = OllamaPool(_settings(), transport)
    result = decide("A new lead has no owner and nobody has replied.", pool=pool)
    assert result["route"] == "rule"
    assert result["escalate_paid"] is False
    assert "Erich" in result["answer"]
    assert result["rule"]

    unknown = decide("What colour should the Kyoto booth fabric contract be?", pool=pool)
    assert unknown["route"] == "escalate"
    assert unknown["escalate_paid"] is True
    assert unknown["reason"]


def test_assign_escalates_when_no_rule_and_no_model():
    def transport(method, url, body, timeout):
        raise urllib.error.URLError("down")

    pool = OllamaPool(_settings(), transport)
    result = assign("What colour should the Kyoto booth fabric contract be?", pool=pool)
    assert result["route"] == "escalate"
    assert result["escalate_paid"] is True
    assert result["owner"] is None


def test_headroom_degrades_when_package_is_absent(monkeypatch):
    import sys
    monkeypatch.setitem(sys.modules, "headroom", None)
    # A failed import (None in sys.modules raises TypeError/ImportError inside the helper).
    assert compress_context("question", "the facts") == "the facts"


def test_headroom_compress_is_used_when_installed(monkeypatch):
    import sys
    import types

    module = types.ModuleType("headroom")

    class Result:
        messages = [{}, {}, {"content": "shrunk facts"}]

    module.compress = lambda messages, model="gpt-4o": Result()
    monkeypatch.setitem(sys.modules, "headroom", module)
    assert compress_context("question", "a long fact list") == "shrunk facts"
