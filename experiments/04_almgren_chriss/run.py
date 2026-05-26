#!/usr/bin/env python3
"""EXP-04: Execution edge with AC impact."""

from __future__ import annotations

import json
from pathlib import Path

from medallion.simulation import CostModel, simulate_execution_edge

RESULTS = Path(__file__).parent / "results"


def main() -> None:
    cost = CostModel(commission_bps=1.0, slippage_bps=2.0)
    m = simulate_execution_edge(cost=cost, edge_bps=0.5, seed=0)
    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "summary.json").write_text(json.dumps(m, indent=2))
    print(json.dumps(m, indent=2))


if __name__ == "__main__":
    main()
