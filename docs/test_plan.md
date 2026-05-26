# Test Plan — v0.1.0

## Automated

| Test | Command | Pass |
|------|---------|------|
| Unit tests | `make test` | All pytest green |
| Claim audit | `make claim-audit` | Zero errors |
| Smoke experiments | `make smoke` | Scripts exit 0 |

## Manual

| Test | Procedure | Pass |
|------|-----------|------|
| Source review | Spot-check CLM-2024-003, 004, 008 (Sharpe, leverage, options) | Ranges/hypothesis labels |
| Simulation sanity | Compare gross vs net Sharpe in experiment results | Net ≤ gross |
| Gate B | Count signals with replication ≠ `not_attempted` | ≥10 in DB (see signals.yaml) |
| Gate C | Verify experiment contracts exist | ≥3 under experiments/ |

## Sensitivity (documented)

- Vary `commission_bps` / `slippage_bps` in experiments 03, 05
- Vary leverage band in experiment 05
- Vary `participation_rate` in experiment 04

Record outcomes in each experiment `results/summary.json`.

## Release checklist (Gate D)

- [ ] Synthesis complete
- [ ] `make reproduce` passes
- [ ] CHANGELOG v0.1.0
- [ ] Git tag v0.1.0
