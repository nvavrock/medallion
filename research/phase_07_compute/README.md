# Phase VII — Computational Reconstruction {#phase-vii-compute}

**Last updated:** 2026-05-28

## Environment

- Python 3.11+
- Package: `medallion` (`pip install -e ".[dev]"`)

## Data policy

- **CI / default:** synthetic-only toys — no network downloads in `make smoke`.
- **Optional local:** [data/manifest.yaml](https://github.com/nvavrock/medallion/blob/main/data/manifest.yaml) FRED/yfinance paths may be populated for exploratory runs; not required for gates.

## Experiment catalog

| ID | Path | Signals | What it proves (directional) |
|----|------|---------|----------------------------|
| EXP-03 | [03_mean_reversion](https://github.com/nvavrock/medallion/tree/main/experiments/03_mean_reversion) | SIG-002 | Costs erode mean-reversion net Sharpe |
| EXP-04 | [04_almgren_chriss](https://github.com/nvavrock/medallion/tree/main/experiments/04_almgren_chriss) | SIG-007 | Impact + fees bind execution-only stories |
| EXP-05 | [05_vol_target_kelly](https://github.com/nvavrock/medallion/tree/main/experiments/05_vol_target_kelly) | SIG-015 | Vol targeting vs costs |
| EXP-06 | [06_variance_risk_premium](https://github.com/nvavrock/medallion/tree/main/experiments/06_variance_risk_premium) | SIG-009 | VRP toy under costs |
| EXP-07 | [07_multi_signal](https://github.com/nvavrock/medallion/tree/main/experiments/07_multi_signal) | SIG-002, SIG-003 | Ensemble vs single sleeve |
| EXP-08 | [08_regime_filter](https://github.com/nvavrock/medallion/tree/main/experiments/08_regime_filter) | SIG-005, SIG-002 | Regime gate meta-signal (not HMM) |

EXP-03/04/05 include **`sensitivity`** blocks in `results/summary.json` (commission, slippage, participation, leverage sweeps).

## Run all

```bash
make smoke
```

Requirement: R7
