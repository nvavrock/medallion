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
- Follow [docs/evidence_rubric.md](docs/evidence_rubric.md) (E0–E4 language, Sharpe/leverage bands).
- Run `make claim-audit` and `make quarto-check` before opening a PR.

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
3. Ensure CI passes (Quarto Publish workflow on merge).

Not investment advice; not affiliated with Renaissance Technologies — see [docs/disclaimer.md](docs/disclaimer.md).
