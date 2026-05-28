"""Tests for QA validators (contracts, summaries, rubric lint)."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

import pytest
import yaml

from medallion.rubric_lint import lint_file
from medallion.paths import ROOT

SCRIPTS = ROOT / "scripts"


def test_validate_experiment_contracts_script():
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "validate_experiment_contracts.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout


def test_validate_experiment_summaries_script():
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "validate_experiment_summaries.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout


def test_rubric_lint_script_strict():
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "rubric_lint.py"), "--strict"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr + proc.stdout


def test_contract_schema_rejects_missing_field():
    import json

    import jsonschema

    from medallion.paths import SCHEMAS_DIR

    schema = json.loads((SCHEMAS_DIR / "experiment_contract.schema.json").read_text())
    bad = {"experiment_id": "EXP-99", "title": "x"}
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.Draft202012Validator(schema).validate(bad)


def test_summary_net_gross_check_logic():
    from scripts.validate_experiment_summaries import check_summary

    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "summary.json"
        p.write_text(
            json.dumps({"gross_sharpe": 0.5, "net_sharpe": 0.9}),
            encoding="utf-8",
        )
        errs = check_summary(p, "03_mean_reversion")
        assert any("net_sharpe" in e for e in errs)


def test_rubric_win_rate_error():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write("Medallion achieved a 51% win rate on trades.\n")
        path = Path(f.name)
    try:
        findings = lint_file(path, db={})
        assert any(f.rule == "forbidden_metric" and f.severity == "error" for f in findings)
    finally:
        path.unlink()


def test_rubric_win_rate_allowed_disclaimer():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
        f.write("Win rate is **not used** as an evidentiary metric.\n")
        path = Path(f.name)
    try:
        findings = lint_file(path, db={})
        assert not any(f.rule == "forbidden_metric" for f in findings)
    finally:
        path.unlink()
