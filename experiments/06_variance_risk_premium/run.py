#!/usr/bin/env python3
"""EXP-06: Variance risk premium toy."""

from __future__ import annotations

import json
from pathlib import Path

from medallion.simulation import CostModel, simulate_variance_risk_premium

RESULTS = Path(__file__).parent / "results"


def main() -> None:
    cost = CostModel(commission_bps=1.0, slippage_bps=2.0)
    baseline = simulate_variance_risk_premium(cost=cost, seed=3)
    sweeps = [
        simulate_variance_risk_premium(cost=CostModel(commission_bps=c, slippage_bps=s), seed=3)
        for c, s in ((0.5, 1.0), (2.0, 4.0))
    ]
    summary = {
        **baseline,
        "sensitivity": {"sweeps": [{"commission_slippage_variant": i, **row} for i, row in enumerate(sweeps)]},
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
