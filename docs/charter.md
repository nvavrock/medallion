# Medallion Fund Reconstruction — Project Charter

## Mission

Build the highest-fidelity **public** reconstruction possible of the scientific, statistical, computational, organizational, and market mechanisms that could plausibly explain Renaissance Technologies’ Medallion Fund historical performance.

This is **quantitative archaeology**: assembling fragmented public evidence, academic analogues, market microstructure theory, historical datasets, and computational experiments into a coherent explanatory framework.

## What We Are Not Doing

- Obtaining or inferring proprietary RenTech systems, source code, or confidential data
- Impersonating Renaissance Technologies or claiming insider knowledge
- Scraping paywalled content without license
- Building live trading or production execution infrastructure

## Success Metrics

| ID | Metric | Target |
|----|--------|--------|
| SM1 | Evidence coverage | Every major assertive claim has an evidence record with rubric fields |
| SM2 | Simulation rigor | Each experiment documents costs, slippage, capacity limits, and known weaknesses |
| SM3 | Phase deliverables | Phases I–VIII research artifacts exist and are cross-linked |
| SM4 | Reproducibility | `make reproduce` runs from a clean environment with pinned dependencies |
| SM5 | PDF review remediation | Sourced vs inferred labeling; options/vol/reg/ML gaps addressed; ranges for leverage/Sharpe |
| SM6 | Public site | Quarto website builds via `make site`; disclaimer on all pages |

## Scope

### In scope

- Phases I–VIII as defined in [medallion_fund_reconstruct.md](../medallion_fund_reconstruct.md)
- Evidence-graded research corpus under `research/`
- **Quarto public website** under `quarto/` (local preview now; GitHub Pages when repo is public)
- Runnable Python experiments under `experiments/` with optional R scripts under `r/`
- Signal Hypothesis Database, Data Availability Matrix, Risk Stack Reconstruction
- Public synthesis with survivorship and regulatory angles (per file review)

### Out of scope

- Proprietary data acquisition
- Live trading APIs
- [slack_problem.md](../slack_problem.md) (unrelated; excluded from Quarto site)

## Work Breakdown (Epics)

| Epic | Phase | Primary deliverable |
|------|-------|---------------------|
| E1 | I | Historical timeline, strategy map, personnel matrix, infra timeline |
| E2 | II | Historical Data Availability Matrix (1980–2025) |
| E3 | III | Signal Hypothesis Database (+ options/volatility, modern ML workstreams) |
| E4 | IV | Microstructure/execution analysis + cost-aware experiment |
| E5 | V | Risk Stack Reconstruction (6 layers) |
| E6 | VI | Organizational comparison matrix |
| E7 | VII | Reproducible computational experiments |
| E8 | VIII | Synthesis, counterarguments, survivorship section |
| E9 | Pub | Quarto website + publishing pipeline |

## Governance

- **Evidence standard:** See [evidence_rubric.md](evidence_rubric.md)
- **Requirements traceability:** See [requirements.md](requirements.md)
- **Publishing:** See [publishing.md](publishing.md)
- **Claim changes:** Log in [CHANGELOG.md](../CHANGELOG.md) with `claim_id`
- **Disclaimer:** See [disclaimer.md](disclaimer.md)

## Milestones

| Milestone | Output |
|-----------|--------|
| M0 | Charter, requirements, rubric |
| M1 | Architecture, Phase I–II |
| M2 | Signal DB, Phase IV experiment |
| M3 | Risk stack, org matrix |
| M4 | Phase VII–VIII, QA pass |
| M5 | Release v0.1.0 (research corpus + code) |
| M6 | Public Quarto site v0.2.0 |

Time is not a primary constraint; depth and accuracy are.

## Stakeholders

- **Readers:** Public audience (educational reconstruction)
- **Contributors:** GitHub collaborators when repo is public
- **Reviewers:** Claim audit, test plan, and Quarto build gates

## Approval

This charter governs scope for release **v0.2.0** and later. Changes require an entry in CHANGELOG.md and, if scope-expanding, an update to requirements.md.
