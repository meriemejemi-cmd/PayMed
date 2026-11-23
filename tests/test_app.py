
from src.app import calculate_risk_score, get_status


def test_risk_for_older_patient():
    assert calculate_risk_score(60, False) == 50


def test_risk_for_smoker():
    assert calculate_risk_score(30, True) == 30


def test_status():
    assert get_status(60) == "HIGH"
def test_low_status():
    assert get_status(30) == "LOW"