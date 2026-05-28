#!/usr/bin/env python3
"""EXP-05: Vol target + banded leverage."""

from __future__ import annotations

import json
from pathlib import Path

from medallion.simulation import CostModel, vol_target_kelly_simulation

RESULTS = Path(__file__).parent / "results"


def _run(
    cost: CostModel,
    leverage_band: tuple[float, float],
    seed: int = 1,
) -> dict:
    return vol_target_kelly_simulation(cost=cost, leverage_band=leverage_band, seed=seed)


def main() -> None:
    baseline_cost = CostModel(commission_bps=1.0, slippage_bps=1.5)
    baseline = _run(baseline_cost, (5.0, 12.0))
    sweeps = []
    for commission_bps in (0.5, 1.0, 2.0):
        c = CostModel(commission_bps=commission_bps, slippage_bps=1.5)
        sweeps.append({"commission_bps": commission_bps, "leverage_band": [5.0, 12.0], **_run(c, (5.0, 12.0))})
    for lo, hi in ((3.0, 8.0), (8.0, 15.0)):
        sweeps.append(
            {
                "commission_bps": 1.0,
                "leverage_band": [lo, hi],
                **_run(baseline_cost, (lo, hi)),
            }
        )
    summary = {
        **baseline,
        "sensitivity": {
            "baseline_params": {"commission_bps": 1.0, "leverage_band": [5.0, 12.0]},
            "sweeps": sweeps,
        },
    }
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
