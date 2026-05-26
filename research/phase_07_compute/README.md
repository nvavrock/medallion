# Phase VII — Computational Reconstruction

## Environment

- Python 3.11+
- Package: `medallion` (`pip install -e ".[dev]"`)

## Experiments

| ID | Path | Linked signals |
|----|------|----------------|
| EXP-03 | [experiments/03_mean_reversion/](../../experiments/03_mean_reversion/) | SIG-002 |
| EXP-04 | [experiments/04_almgren_chriss/](../../experiments/04_almgren_chriss/) | SIG-007 |
| EXP-05 | [experiments/05_vol_target_kelly/](../../experiments/05_vol_target_kelly/) | SIG-015 |
| EXP-07 | [experiments/07_multi_signal/](../../experiments/07_multi_signal/) | SIG-002, SIG-003 |

Each experiment includes `contract.yaml` per schema.

## Run all

```bash
make smoke
```

Requirement: R7
