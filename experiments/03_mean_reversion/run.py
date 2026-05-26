#!/usr/bin/env python3
"""EXP-03: Mean reversion backtest with costs."""

from __future__ import annotations

import json
from pathlib import Path

from medallion.simulation import CostModel, simulate_mean_reversion

RESULTS = Path(__file__).parent / "results"


def main() -> None:
    cost = CostModel(commission_bps=1.0, slippage_bps=2.0)
    r = simulate_mean_reversion(cost=cost, seed=42)
    RESULTS.mkdir(exist_ok=True)
    summary = {
        "gross_sharpe": r.gross_sharpe,
        "net_sharpe": r.net_sharpe,
        "max_drawdown": r.max_drawdown,
        "turnover": r.turnover,
        "capacity_breach_pct": r.capacity_breach_pct,
    }
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
