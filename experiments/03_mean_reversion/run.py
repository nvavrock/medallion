#!/usr/bin/env python3
"""EXP-03: Mean reversion backtest with costs."""

from __future__ import annotations

import json
from pathlib import Path

from medallion.simulation import CostModel, simulate_mean_reversion

RESULTS = Path(__file__).parent / "results"


def _run(cost: CostModel, seed: int = 42) -> dict:
    r = simulate_mean_reversion(cost=cost, seed=seed)
    return {
        "gross_sharpe": r.gross_sharpe,
        "net_sharpe": r.net_sharpe,
        "max_drawdown": r.max_drawdown,
        "turnover": r.turnover,
        "capacity_breach_pct": r.capacity_breach_pct,
    }


def main() -> None:
    baseline_cost = CostModel(commission_bps=1.0, slippage_bps=2.0)
    baseline = _run(baseline_cost)
    sweeps = []
    for commission_bps in (0.5, 1.0, 2.0):
        for slippage_bps in (1.0, 2.0, 4.0):
            c = CostModel(commission_bps=commission_bps, slippage_bps=slippage_bps)
            row = _run(c)
            sweeps.append(
                {
                    "commission_bps": commission_bps,
                    "slippage_bps": slippage_bps,
                    **row,
                }
            )
    summary = {
        **baseline,
        "sensitivity": {"baseline_params": {"commission_bps": 1.0, "slippage_bps": 2.0}, "sweeps": sweeps},
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
