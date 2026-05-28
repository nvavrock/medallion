# Test Plan — v1.0.0

## Automated

| Test | Command | Pass |
|------|---------|------|
| Unit tests | `make test` | All pytest green |
| Claim audit | `make claim-audit` | Zero errors |
| Evidence coverage | `make quarto-check` (`validate_evidence_coverage.py`) | Zero orphan active claims |
| Data matrix (Gate A) | `make quarto-check` | Zero errors |
| Signal DB (Gate B) | `make quarto-check` | ≥10 signals attempted |
| Quarto links | `make quarto-check` | Zero unresolved link warnings |
| Smoke experiments | `make smoke` | 6 experiments exit 0 |
| Quarto build (Gate E) | `make site` | Render succeeds |

## Manual

| Test | Procedure | Pass |
|------|-----------|------|
| Source review | CLM-2024-003, 004, 008 in risk/synthesis/options | Ranges / E1 labels |
| Simulation sanity | EXP-03/05 gross vs net | Net ≤ gross |
| Live site | Phase II anchors, synthesis corpus map | Links work on Pages |

## Sensitivity (automated in summary.json)

- EXP-03: `commission_bps`, `slippage_bps`
- EXP-04: `participation_rate`
- EXP-05: `commission_bps`, `leverage_band`

## Release checklist (Gate D) — v1.0.0

- [x] Epics 2–5 complete per [docs/traceability.md](traceability.md)
- [x] `make reproduce` + `make quarto-check` + `make site`
- [x] CHANGELOG v1.0.0; tag v1.0.0
- [x] GitHub Pages live

## Review gates summary

| Gate | Status |
|------|--------|
| A–E, D | Pass |
