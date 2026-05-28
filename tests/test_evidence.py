import subprocess
import sys
from pathlib import Path

import yaml

from medallion.evidence import audit_claims, load_evidence
from medallion.signals import audit_gate_b, load_signals, signals_by_tag

ROOT = Path(__file__).resolve().parents[1]


def test_load_evidence():
    claims = load_evidence()
    assert len(claims) >= 45
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


def test_data_matrix_row_count():
    raw = yaml.safe_load(
        (ROOT / "research" / "phase_02_data" / "data_availability_matrix.yaml").read_text(
            encoding="utf-8"
        )
    )
    assert len(raw["datasets"]) >= 25


def test_validate_data_matrix_script():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_data_matrix.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr


def test_gate_b_replication():
    assert audit_gate_b() == []


def test_validate_signals_script():
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_signals.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
