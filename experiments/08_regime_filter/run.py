#!/usr/bin/env python3
"""EXP-08: Regime-gated ensemble toy."""

from __future__ import annotations

import json
from pathlib import Path

from medallion.simulation import CostModel, simulate_regime_gated_ensemble

RESULTS = Path(__file__).parent / "results"


def main() -> None:
    cost = CostModel(commission_bps=1.5, slippage_bps=2.5)
    summary = simulate_regime_gated_ensemble(cost=cost, seed=11)
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
