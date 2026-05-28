# Requirements traceability

**Last updated:** 2026-05-28 (v1.0.0)

| ID | Deliverable | Path | Gate |
|----|-------------|------|------|
| R1 | Timeline | research/phase_01_history/timeline.md | M1 |
| R1b | Strategy evolution | research/phase_01_history/strategy_evolution.md | M1 |
| R1c | Personnel matrix | research/phase_01_history/personnel_matrix.md | M1 |
| R1d | Infrastructure timeline | research/phase_01_history/infrastructure_timeline.md | M1 |
| R2 | Data matrix | research/phase_02_data/data_availability_matrix.yaml | A |
| R3 | Signal DB | data/signals.yaml | B |
| R3a | Options/vol | research/phase_03_signals/options_vol.md | B |
| R3b | Modern ML | research/phase_03_signals/modern_ml.md | B |
| R4 | Execution analysis | research/phase_04_execution/ | M2 depth |
| R4b | AC experiment | experiments/04_almgren_chriss/ | C |
| R5 | Risk stack | research/phase_05_risk/ | M3 depth |
| R5b | Vol-target experiment | experiments/05_vol_target_kelly/ | C |
| R6 | Org matrix | research/phase_06_org/ | M3 depth |
| R7 | Experiments | experiments/03–08 | C (≥6) |
| R8 | Synthesis | research/phase_08_synthesis/ | D |
| R9 | Quarto site | quarto/ | E |
| NFR1 | Claim audit | scripts/claim_audit.py, validate_evidence_coverage.py | quarto-check |
| NFR2 | Costs in sims | experiments/*/contract.yaml | smoke |
| NFR3 | Rubric language | docs/evidence_rubric.md | manual |
| NFR4 | Bibliography | data/bibliography.yaml → quarto/references.bib | quarto-assets |
| NFR5 | Reproduce | Makefile `reproduce` | CI |
| NFR6 | Disclaimer | quarto/index.qmd, about.qmd | E |
| NFR7 | Claim refs | quarto/filters/claim-refs.lua | site build |
