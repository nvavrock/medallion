# Test Plan — v0.6.0

## Automated

| Test | Command | Pass |
|------|---------|------|
| Unit tests | `make test` | All pytest green |
| Claim audit | `make claim-audit` | Zero errors |
| Data matrix (Gate A) | `make quarto-check` (includes `validate_data_matrix.py`) | Zero errors |
| Signal DB (Gate B) | `make quarto-check` (includes `validate_signals.py`) | ≥10 signals with replication ≠ `not_attempted` |
| Quarto links | `make quarto-check` (includes `check_quarto_warnings.sh`) | Zero unresolved link warnings |
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
| Live site links | Phase II reading order on GitHub Pages | In-chapter anchors work |

## Sensitivity (documented)

- Vary `commission_bps` / `slippage_bps` in experiments 03, 05
- Vary leverage band in experiment 05
- Vary `participation_rate` in experiment 04

Record outcomes in each experiment `results/summary.json`.

## Release checklist (Gate D) — v0.6.0

- [x] Synthesis expanded (v0.5.0)
- [x] Phase III–VI narrative depth (v0.5.0)
- [x] Gate B automated (`scripts/validate_signals.py`)
- [x] `make reproduce` passes
- [x] Quarto cross-links fixed (`scripts/check_quarto_warnings.sh`)
- [x] CI runs `make reproduce` before site deploy
- [x] CHANGELOG v0.6.0
- [x] Git tag v0.6.0
- [x] Repository public + GitHub Pages live ([publishing.md](publishing.md))

## Review gates summary

| Gate | Status (v0.6.0) |
|------|-----------------|
| A | Pass — 28-row data matrix |
| B | Pass — 15/15 signals attempted (automated) |
| C | Pass — 4 experiments with contracts |
| D | Pass — synthesis, audit, reproduce, v0.6.0 tag, live site |
| E | Pass — https://nvavrock.github.io/medallion/ |
