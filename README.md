# Medallion Fund Reconstruction

Evidence-driven internal research project to reconstruct plausible operating principles behind Renaissance Technologies' Medallion Fund using **public sources only**.

See [docs/charter.md](docs/charter.md) and [docs/disclaimer.md](docs/disclaimer.md).

## Quick start

**Prerequisites:** Python 3.11+ and either [uv](https://docs.astral.sh/uv/) (recommended) or the OS `python3-venv` package:

```bash
# Debian/Ubuntu if you do not use uv:
sudo apt install python3-venv
```

```bash
make install      # creates .venv and installs dependencies
make reproduce    # tests, claim audit, and smoke experiments
```

If a previous `make install` failed, remove the broken venv first: `make clean && make install`

## Structure

| Path | Purpose |
|------|---------|
| `docs/` | SDLC docs (charter, requirements, rubric, architecture, test plan) |
| `research/` | Phase I–VIII write-ups |
| `data/` | Evidence DB, signal DB, bibliography |
| `src/medallion/` | Python library (evidence, signals, simulation) |
| `experiments/` | Reproducible hypothesis tests |
| `schemas/` | JSON Schema validation |

## Evidence citations

In research markdown: `[[claim:CLM-2024-001]]`

Run audit: `make claim-audit`

## Release

Internal **v0.1.0** — see [CHANGELOG.md](CHANGELOG.md).
