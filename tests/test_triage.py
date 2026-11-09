"""HQ rubric and standing owner rules. No model."""

import json
import re

import pytest

from brain.triage import CLOSER, NONE, WALKTHROUGH, triage_lead


def test_owned_lead_stays_with_owner():
    result = triage_lead({
        "owner": "Andries",
        "practice": True,
        "patients_per_month": 40,
        "setting": "medical",
        "country": "ZA",
    })
    assert result["owner"] == "Andries"
    assert result["hq"] is False
    assert result["calendar"] == WALKTHROUGH
    assert result["product"] == "Neuro"
    assert result["route"] == "rule"
    assert result["escalate_paid"] is False


def test_unowned_goes_to_erich_and_over_100_is_closer_hq():
    result = triage_lead({
        "owner": None,
        "practice": True,
        "patients_per_month": 150,
        "setting": "aesthetics",
    })
    assert result["owner"] == "Erich"
    assert result["hq"] is True
    assert result["calendar"] == CLOSER
    assert result["product"] == "Optimum"


def test_exactly_100_patients_is_not_over_the_gate():
    result = triage_lead({
        "owner": "Hazel",
        "practice": True,
        "patients_per_month": 100,
        "setting": "medical",
    })
    assert result["hq"] is False
    assert result["calendar"] == WALKTHROUGH
    assert result["owner"] == "Hazel"


def test_buyer_goes_to_davide_and_output_has_no_price():
    result = triage_lead({
        "owner": "Hazel",
        "buying_intent": True,
        "country": "ZA",
        "message": "how much does it cost, I want to start",
    })
    assert result["owner"] == "Davide"
    assert result["record_owner"] == "Hazel"
    assert result["no_sa_pricing"] is True
    assert result["calendar"] == NONE
    blob = json.dumps(result)
    assert not re.search(r"R\s?\d", blob)
    assert "15000" not in blob
    assert "[price]" not in blob


def test_us_lead_is_email_only_and_keeps_owner():
    result = triage_lead({
        "country": "US",
        "owner": "Eddie",
        "practice": True,
        "patients_per_month": 200,
        "channel_requested": "sms",
        "setting": "medical",
    })
    assert result["channel"] == "email"
    assert result["channel_blocked"] is True
    assert result["owner"] == "Eddie"
    assert result["hq"] is True
    assert result["calendar"] == CLOSER
    assert result["product"] == "Neuro"
    assert "sms" not in result["channel"]


def test_patient_is_not_hq():
    result = triage_lead({"patient_use": True, "owner": "Eddie", "country": "ZA"})
    assert result["hq"] is False
    assert result["calendar"] == NONE
    assert result["owner"] == "Eddie"
    assert result["do_not_contact"] is False


def test_opt_out_is_not_contacted():
    result = triage_lead({"opted_out": True, "owner": "Michael", "patients_per_month": 400})
    assert result["hq"] is False
    assert result["calendar"] == NONE
    assert result["do_not_contact"] is True
    assert result["owner"] == "Michael"


def test_partner_is_not_hq():
    result = triage_lead({"partner": True, "owner": "Ian", "patients_per_month": 500, "practice": True})
    assert result["hq"] is False
    assert result["calendar"] == NONE
    assert result["owner"] == "Ian"


@pytest.mark.parametrize("setting,product", [("aesthetics", "Optimum"), ("medical", "Neuro")])
def test_product_by_setting(setting, product):
    result = triage_lead({"practice": True, "patients_per_month": 10, "setting": setting, "owner": "Erich"})
    assert result["product"] == product
