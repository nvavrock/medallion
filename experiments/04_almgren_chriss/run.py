#!/usr/bin/env python3
"""EXP-04: Execution edge with AC impact."""

from __future__ import annotations

import json
from pathlib import Path

from medallion.simulation import CostModel, simulate_execution_edge

RESULTS = Path(__file__).parent / "results"


def _run(participation_rate: float, cost: CostModel) -> dict:
    return simulate_execution_edge(
        cost=cost, edge_bps=0.5, participation_rate=participation_rate, seed=0
    )


def main() -> None:
    cost = CostModel(commission_bps=1.0, slippage_bps=2.0)
    baseline = _run(0.01, cost)
    sweeps = [
        {"participation_rate": p, **_run(p, cost)}
        for p in (0.005, 0.01, 0.02, 0.05)
    ]
    summary = {
        **baseline,
        "sensitivity": {"baseline_params": {"participation_rate": 0.01}, "sweeps": sweeps},
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
