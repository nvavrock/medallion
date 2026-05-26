from medallion.evidence import audit_claims, load_evidence
from medallion.signals import load_signals, signals_by_tag


def test_load_evidence():
    claims = load_evidence()
    assert len(claims) >= 10
    assert all(c.claim_id.startswith("CLM-") for c in claims)


def test_load_signals():
    signals = load_signals()
    assert len(signals) >= 10


def test_options_workstream():
    vol = signals_by_tag("volatility")
    assert len(vol) >= 3


def test_ml_workstream():
    ml = signals_by_tag("ml")
    assert len(ml) >= 3


def test_claim_audit_no_errors():
    errors, _ = audit_claims()
    assert errors == []
