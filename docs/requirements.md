# Requirements — Medallion Fund Reconstruction

Traceability: each requirement links to `research/` folders, `quarto/`, and optional `experiments/`.

## Functional Requirements

| ID | Requirement | Phase | Deliverable path | Acceptance criteria |
|----|-------------|-------|------------------|---------------------|
| R1 | Chronological timeline of RenTech / Medallion | I | `research/phase_01_history/timeline.md` | Major events 1978–2025 with sources |
| R1b | Strategy evolution map | I | `research/phase_01_history/strategy_evolution.md` | Currencies → futures → stat arb transitions |
| R1c | Personnel contribution matrix | I | `research/phase_01_history/personnel_matrix.md` | Simons, Berlekamp, Mercer, Brown, Patterson |
| R1d | Infrastructure timeline | I | `research/phase_01_history/infrastructure_timeline.md` | Compute/data milestones |
| R2 | Historical Data Availability Matrix (1980–2025) | II | `research/phase_02_data/data_availability_matrix.yaml` | Fields: earliest_year, cost, storage, compute, coverage, latency, viability |
| R3 | Signal Hypothesis Database | III | `data/signals.yaml` | Columns: signal, theory, evidence, replication, capacity, confidence |
| R3a | Options/volatility workstream | III | `data/signals.yaml` (tags) | At least 3 options/vol signals with era plausibility |
| R3b | Modern ML/NLP workstream | III | `data/signals.yaml` (tags) | At least 2 ML signals with era feasibility notes |
| R4 | Microstructure & execution analysis | IV | `research/phase_04_execution/README.md` | Models cited; answers “execution edge alone?” |
| R4b | Cost-aware microstructure experiment | IV | `experiments/04_almgren_chriss/` | Experiment contract + results with costs |
| R5 | Risk Stack Reconstruction (6 layers) | V | `research/phase_05_risk/risk_stack.md` | Signal → tail-risk layers documented |
| R5b | Vol-target / Kelly-variant simulation | V | `experiments/05_vol_target_kelly/` | Banded leverage; costs included |
| R6 | Org comparison matrix | VI | `research/phase_06_org/comparison_matrix.md` | vs Two Sigma, DE Shaw, Citadel |
| R7 | Reproducible experiments (Python) | VII | `experiments/*` | Pinned deps; README per experiment |
| R8 | Synthesis with counterarguments | VIII | `research/phase_08_synthesis/synthesis.md` | Integrates phases; survivorship; regulatory section |
| R9 | Quarto public website | Pub | `quarto/` | `make site` succeeds; disclaimer on index and about |

## Non-Functional Requirements (NFR)

| ID | Requirement | Verification |
|----|-------------|--------------|
| NFR1 | Every major claim has evidence metadata | `make claim-audit` passes |
| NFR2 | Simulations include transaction costs, slippage, capacity | Experiment contracts + code review |
| NFR3 | Sourced vs inferred language per rubric | Manual spot-check + audit |
| NFR4 | Normalized bibliography | `data/bibliography.yaml` → `quarto/references.bib` |
| NFR5 | Reproducible environment | `make reproduce` from clean venv |
| NFR6 | Public disclaimer on Quarto site | `index.qmd` + `about.qmd` link to disclaimer |
| NFR7 | Claim refs resolve in Quarto | `claim-refs.lua` filter; build fails on unknown IDs |

## PDF Review Remediation (acceptance)

| Item | Requirement ID | Status target |
|------|----------------|---------------|
| Label sourced vs inferred | NFR3, rubric | All high-impact metrics use ranges/hypothesis labels |
| Options/volatility coverage | R3a | Signals in DB |
| Regulatory/structural edges | R8 | Section in synthesis |
| Modern ML/NLP | R3b | Signals in DB |
| Failed peers (LTCM, etc.) | R8 | Survivorship section |
| Simulation rigor (not coin-flip only) | NFR2, R7 | ≥3 cost-aware experiments |
| Reduce repetition | NFR3 | No duplicate win-rate mantra without new evidence |
| Citation cleanup | NFR4 | Bibliography in Quarto |

## Review Gates

| Gate | After | Pass criteria |
|------|-------|---------------|
| A | Phase II | Core asset classes in data matrix |
| B | Phase III | ≥10 signals with replication field filled |
| C | Phase VII | ≥3 experiments with full contracts |
| D | Release | Synthesis + claim audit + `make test` |
| E | Quarto | `make site` + NFR6–NFR7 |

## Out of Scope

See [charter.md](charter.md).
