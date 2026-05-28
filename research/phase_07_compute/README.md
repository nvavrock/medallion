# Phase VII — Computational Reconstruction

## Environment

- Python 3.11+
- Package: `medallion` (`pip install -e ".[dev]"`)

## Experiments

| ID | Path | Linked signals |
|----|------|----------------|
| EXP-03 | [03_mean_reversion](https://github.com/nvavrock/medallion/tree/main/experiments/03_mean_reversion) | SIG-002 |
| EXP-04 | [04_almgren_chriss](https://github.com/nvavrock/medallion/tree/main/experiments/04_almgren_chriss) | SIG-007 |
| EXP-05 | [05_vol_target_kelly](https://github.com/nvavrock/medallion/tree/main/experiments/05_vol_target_kelly) | SIG-015 |
| EXP-07 | [07_multi_signal](https://github.com/nvavrock/medallion/tree/main/experiments/07_multi_signal) | SIG-002, SIG-003 |

Each experiment includes `contract.yaml` per schema.

## Run all

```bash
make smoke
```

Requirement: R7
