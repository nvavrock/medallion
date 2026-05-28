# Test Plan — v0.5.0

## Automated

| Test | Command | Pass |
|------|---------|------|
| Unit tests | `make test` | All pytest green |
| Claim audit | `make claim-audit` | Zero errors |
| Data matrix (Gate A) | `make quarto-check` (includes `validate_data_matrix.py`) | Zero errors |
| Signal DB (Gate B) | `make quarto-check` (includes `validate_signals.py`) | ≥10 signals with replication ≠ `not_attempted` |
| Smoke experiments | `make smoke` | Scripts exit 0 |
| Quarto build (Gate E) | `make site` | Render succeeds; claim refs resolve |

## Manual

| Test | Procedure | Pass |
|------|-----------|------|
| Source review | Spot-check CLM-2024-003, 004, 008 (Sharpe, leverage, options) | Ranges/hypothesis labels in synthesis and risk stack |
| Simulation sanity | Compare gross vs net Sharpe in experiment results | Net ≤ gross |
| Gate C | Verify experiment contracts exist | ≥3 under experiments/ (EXP-03, 04, 05, 07) |
| Phase III depth | Read core_stat_arb, options_vol, modern_ml essays | Each links signal IDs + matrix rows |
| Disclaimer (NFR6) | Open built `index.html` and `about.html` | Disclaimer linked |

## Sensitivity (documented)

- Vary `commission_bps` / `slippage_bps` in experiments 03, 05
- Vary leverage band in experiment 05
- Vary `participation_rate` in experiment 04

Record outcomes in each experiment `results/summary.json`.

## Release checklist (Gate D) — v0.5.0

- [x] Synthesis expanded (ranges, counterarguments, no win-rate mantra)
- [x] Phase III–VI narrative depth
- [x] Gate B automated (`scripts/validate_signals.py`)
- [ ] `make reproduce` passes on maintainer machine
- [x] CHANGELOG v0.5.0
- [ ] Git tag v0.5.0 (after merge)
- [x] Repository public + GitHub Pages enabled (M6; see [publishing.md](publishing.md))

## Review gates summary

| Gate | Status (v0.5.0) |
|------|-----------------|
| A | Pass — 28-row data matrix |
| B | Pass — 15/15 signals attempted (automated) |
| C | Pass — 4 experiments with contracts |
| D | Pending tag + public launch |
| E | Pass locally; Pages on push when repo public |
