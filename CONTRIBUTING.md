# Contributing

Thank you for helping improve this **public reconstruction** project.

## Setup

```bash
make install
make reproduce   # tests, claim audit, experiments
make site        # Quarto site (requires Quarto CLI)
```

See [docs/agent-git-policy.md](docs/agent-git-policy.md) for commit/tag conventions.

## Evidence and claims

- Assertive statements in `research/` must use `[[claim:CLM-...]]` with a record in [data/evidence.yaml](data/evidence.yaml).
- Add bibliography keys to [data/bibliography.yaml](data/bibliography.yaml) before citing; use Pandoc syntax `[@key]` in prose.
- Follow [docs/evidence_rubric.md](docs/evidence_rubric.md) (E0–E4 language, Sharpe/leverage bands).
- Run `make qa` before opening a PR (same gates as [CI](.github/workflows/ci.yml): `reproduce` + `quarto-check`).

## Signals and data matrix

- Signal changes: [data/signals.yaml](data/signals.yaml) + [schemas/signal_hypothesis.schema.json](schemas/signal_hypothesis.schema.json).
- Data matrix rows: [research/phase_02_data/data_availability_matrix.yaml](research/phase_02_data/data_availability_matrix.yaml) — update evidence claims first.

## Experiments

- Add `contract.yaml`, `run.py`, `README.md` under `experiments/NN_name/`.
- Include costs and document limitations; link `linked_signals`.
- Register external data in [data/manifest.yaml](data/manifest.yaml) if not synthetic.

## Pull requests

1. Fork and branch from `main`.
2. Keep scope focused; update [CHANGELOG.md](CHANGELOG.md) for user-visible changes.
3. Ensure **CI** passes on the PR (`make reproduce` + `make quarto-check`). Merges to `main` also run **Quarto Publish** (full site + Pages).

Not investment advice; not affiliated with Renaissance Technologies — see [docs/disclaimer.md](docs/disclaimer.md).
