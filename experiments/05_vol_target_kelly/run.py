#!/usr/bin/env python3
"""EXP-05: Vol target + banded leverage."""

from __future__ import annotations

import json
from pathlib import Path

from medallion.simulation import CostModel, vol_target_kelly_simulation

RESULTS = Path(__file__).parent / "results"


def main() -> None:
    cost = CostModel(commission_bps=1.0, slippage_bps=1.5)
    m = vol_target_kelly_simulation(cost=cost, leverage_band=(5.0, 12.0), seed=1)
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "summary.json").write_text(json.dumps(m, indent=2))
    print(json.dumps(m, indent=2))


if __name__ == "__main__":
    main()
