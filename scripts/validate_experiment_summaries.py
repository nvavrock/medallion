#!/usr/bin/env python3
"""Validate frozen experiment summary.json files from smoke runs."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from medallion.paths import EXPERIMENTS_DIR

SMOKE_DIRS = (
    "03_mean_reversion",
    "04_almgren_chriss",
    "05_vol_target_kelly",
    "06_variance_risk_premium",
    "07_multi_signal",
    "08_regime_filter",
)

SENSITIVITY_REQUIRED = {"03_mean_reversion", "04_almgren_chriss", "05_vol_target_kelly"}

TOL = 1e-6


def check_summary(path: Path, exp_dir: str) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        errors.append(f"{exp_dir}: missing results/summary.json (run make smoke)")
        return errors

    data = json.loads(path.read_text(encoding="utf-8"))
    gross = data.get("gross_sharpe")
    net = data.get("net_sharpe")
    if gross is not None and net is not None:
        if net > gross + TOL:
            errors.append(
                f"{exp_dir}: net_sharpe ({net}) > gross_sharpe ({gross})"
            )

    if exp_dir in SENSITIVITY_REQUIRED:
        sens = data.get("sensitivity") or {}
        sweeps = sens.get("sweeps") if isinstance(sens, dict) else None
        if not sweeps:
            errors.append(f"{exp_dir}: sensitivity.sweeps must be non-empty")

    return errors


def main() -> int:
    errors: list[str] = []
    for exp_dir in SMOKE_DIRS:
        summary_path = EXPERIMENTS_DIR / exp_dir / "results" / "summary.json"
        errors.extend(check_summary(summary_path, exp_dir))

    if errors:
        for msg in errors:
            print(f"ERROR: {msg}", file=sys.stderr)
        print(f"\nExperiment summary validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Experiment summaries passed ({len(SMOKE_DIRS)} smoke experiment(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
