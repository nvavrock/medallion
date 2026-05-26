#!/usr/bin/env python3
"""EXP-07: Multi-signal ensemble (mean reversion + momentum proxy)."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from medallion.simulation import CostModel, simulate_mean_reversion

RESULTS = Path(__file__).parent / "results"


def momentum_sleeve(n_days: int, seed: int, cost: CostModel) -> float:
    rng = np.random.default_rng(seed)
    ret = rng.normal(0.0003, 0.01, n_days)
    signal = pd.Series(ret).rolling(60).mean().shift(1).fillna(0)
    pos = np.sign(signal)
    gross = pos * ret
    turnover = pd.Series(pos).diff().abs().fillna(0)
    net = gross - turnover * cost.round_trip_cost()
    s = pd.Series(net)
    return float(s.mean() / s.std() * np.sqrt(252)) if s.std() > 0 else 0.0


def main() -> None:
    cost = CostModel(commission_bps=1.5, slippage_bps=2.5)
    mr = simulate_mean_reversion(cost=cost, seed=10)
    mom = momentum_sleeve(1260, 20, cost)
    ensemble = (mr.net_sharpe + mom) / 2
    summary = {
        "mean_reversion_net_sharpe": mr.net_sharpe,
        "momentum_net_sharpe": mom,
        "ensemble_net_sharpe": ensemble,
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
