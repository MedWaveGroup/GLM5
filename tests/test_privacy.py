"""Redaction keeps Slack and HighLevel ids and strips contact details."""

from brain.privacy import leaks, redact


def test_redacts_phone_and_bare_mailbox():
    number = "+1 " + "214" + " " + "425" + " " + "0494"
    raw = (
        f"Anthony Polenski: anthony@, {number}. "
        "Janae is janae@. Ian is ian@. Company sender is info@."
    )
    clean = redact(raw)
    assert number not in clean
    assert "anthony@" not in clean
    assert "janae@" not in clean
    assert "ian@" not in clean
    assert "info@" not in clean
    assert "[phone]" in clean
    assert "[email]" in clean
    assert leaks(clean) == []


def test_keeps_slack_and_highlevel_ids():
    raw = "Francois U06TXP9D7BR owns the thread. Contact L6MDCKJ42pYLi2zWFLnL."
    clean = redact(raw)
    assert "U06TXP9D7BR" in clean
    assert "L6MDCKJ42pYLi2zWFLnL" in clean


def test_redacts_secret_shapes_without_touching_the_word_token_alone():
    raw = "token spend is paused. api_key=abc123def was in the dump. sk_live_abcdefghij too."
    clean = redact(raw)
    assert "abc123def" not in clean
    assert "sk_live_abcdefghij" not in clean
    assert "token spend" in clean
