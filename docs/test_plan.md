# Test Plan — v1.0.1

## Automated (single entry)

| Test | Command | Pass |
|------|---------|------|
| **Full QA (gates A–D)** | `make qa` | `reproduce` + `quarto-check` green |
| **Full QA + render (A–E)** | `make qa-full` | Above + `make site` |
| Unit tests | `make test` | All pytest green |
| Claim audit | `make claim-audit` | Zero errors |
| Evidence coverage | `make quarto-check` | Zero orphan active claims |
| Data matrix (Gate A) | `make quarto-check` | Zero errors |
| Signal DB (Gate B) | `make quarto-check` | ≥10 signals attempted |
| Experiment contracts | `make quarto-check` | All `contract.yaml` valid |
| Experiment summaries | `make quarto-check` | net ≤ gross; sensitivity on EXP-03/04/05 |
| Rubric lint | `make quarto-check` (`rubric_lint.py --strict`) | Zero errors/warnings |
| Quarto links | `make quarto-check` | Zero unresolved link warnings |
| Smoke experiments | `make smoke` | 6 experiments exit 0 |
| Quarto build (Gate E) | `make site` | Render succeeds |

## CI

| Workflow | Trigger | Scope |
|----------|---------|-------|
| [ci.yml](../.github/workflows/ci.yml) | PR + push `main` | `make reproduce`, `make quarto-check` |
| [quarto-publish.yml](../.github/workflows/quarto-publish.yml) | push `main` | Above + `make site` + Pages deploy |
| [link-check.yml](../.github/workflows/link-check.yml) | weekly + manual | Live github.io crawl (non-blocking) |

## Manual

See [qa_manual_checklist.md](qa_manual_checklist.md).

| Test | Procedure | Pass |
|------|-----------|------|
| Source review | CLM-2024-003, 004, 008 in risk/synthesis/options | Ranges / E1 labels |
| Synthesis | synthesis.md + experiment_integration.md | No overclaiming |
| Live site | Corpus map, Phase II anchors | Links work on Pages |
| Evidence sample | `scripts/sample_evidence.py` | Level matches prose |

## Sensitivity (automated in summary.json)

- EXP-03: `commission_bps`, `slippage_bps`
- EXP-04: `participation_rate`
- EXP-05: `commission_bps`, `leverage_band`

## Release checklist (Gate D)

- [ ] `make qa-full` on release branch
- [ ] Manual checklist in [qa_manual_checklist.md](qa_manual_checklist.md)
- [ ] CHANGELOG version bump; tag
- [ ] GitHub Pages deploy green

## Review gates summary

| Gate | Automation |
|------|------------|
| A | `validate_data_matrix.py` |
| B | `validate_signals.py` |
| C | `make smoke` + summary/contract validators |
| D | Manual + traceability |
| E | `make site` / Quarto Publish |
