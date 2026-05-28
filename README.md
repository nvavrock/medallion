# Medallion Fund Reconstruction

[![Release](https://img.shields.io/github/v/tag/nvavrock/medallion?label=release)](https://github.com/nvavrock/medallion/releases)
[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/research-CC%20BY--NC%204.0-lightgrey.svg)](LICENSE-CONTENT)

Public, evidence-driven reconstruction of plausible operating principles behind Renaissance Technologies’ Medallion Fund—**public sources only**, with reproducible experiments and a [Quarto](https://quarto.org/) research site.

> **Site (live):** [https://nvavrock.github.io/medallion/](https://nvavrock.github.io/medallion/) — also build locally with `make site` / `make preview`.

See [docs/disclaimer.md](docs/disclaimer.md) — not investment advice; not affiliated with RenTech.

## Quick start

**Prerequisites:** Python 3.11+, [Quarto](https://quarto.org/docs/get-started/), and [uv](https://docs.astral.sh/uv/) (recommended) or `python3-venv`.

If `make site` says Quarto is missing but you installed it locally:

```bash
export PATH="$HOME/.local/quarto/bin:$PATH"
```

```bash
sudo apt install python3-venv   # if not using uv
```

```bash
make install       # Python deps
make qa            # tests, claim audit, validators, experiments (gates A–D)
make site          # build Quarto website (Gate E)
make preview       # live preview of the site
```

Before a PR: `make qa` (CI runs the same checks without a full site render).

## Structure

| Path | Purpose |
|------|---------|
| `quarto/` | Public Quarto website (chapters, appendices) |
| `docs/` | Charter, requirements, [publishing](docs/publishing.md) |
| `research/` | Phase I–VIII source markdown (included by Quarto) |
| `data/` | Evidence DB, signal DB, bibliography |
| `src/medallion/` | Python library |
| `experiments/` | Reproducible hypothesis tests |

## Evidence citations

In research markdown: `[[claim:CLM-2024-001]]` → links to the [evidence registry](quarto/appendices/evidence-registry.qmd) in the built site.

```bash
make claim-audit
```

## Releases

- **v1.0.1** — QA suite: `make qa`, PR CI, contract/rubric validators, manual checklist — [CHANGELOG.md](CHANGELOG.md)
- **v1.0.0** — Charter-complete corpus (Epics 2–5): evidence coverage, phase depth, 6 experiments — [CHANGELOG.md](CHANGELOG.md) · [CONTRIBUTING.md](CONTRIBUTING.md)
- **v0.6.0** — Quarto link fixes, CI `make reproduce`, Gate D closure
- **v0.5.0** — Phase III–VI depth, Gate B automation, synthesis remediation
- **v0.4.0** — Phase II data architecture matrix and narratives
- **v0.2.0** — Public Quarto site (preview; enable Pages when repo is public)
- **v0.1.0** — Research corpus + code
