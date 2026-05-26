# Changelog

## [0.3.0] - 2026-05-26

### Added

- Phase I historical chapter depth: expanded timeline, strategy evolution, personnel matrix, infrastructure timeline, and phase README hub
- Twenty-one new evidence records (CLM-2026-001–021) plus refined CLM-2024-001/005/006; bibliography keys for Wikipedia, Berkeley obituary, and SEC IAPD

### Changed

- Corrected public IBM hire timeline for Brown/Mercer to **1993** (was sometimes misstated as late 1990s)
- Phase II cross-links from Phase I use repo-root-relative paths for Quarto
- SIG-013 era plausibility text aligned to 1993+

## [0.2.0] - 2026-05-26

### Added

- Quarto public website (`quarto/`) with 8 research chapters and appendices
- `claim-refs.lua` filter for evidence claim links
- `scripts/build_quarto_assets.py` (bibliography, appendices, claims map)
- `make site`, `make preview`, `docs/publishing.md`
- GitHub Actions workflow `quarto-publish.yml` (workflow_dispatch until repo is public)
- Dual license: MIT (code), CC BY-NC 4.0 (research/site)

### Changed

- Project framing: internal → public-facing (charter, disclaimer, README, requirements)
- Architecture docs include Quarto publication pipeline

## [0.1.0] - 2026-05-26

### Added

- SDLC documentation (charter, requirements, evidence rubric, architecture, test plan)
- Evidence database (`data/evidence.yaml`) with claim audit tooling
- Signal Hypothesis Database (`data/signals.yaml`) including options/volatility and ML workstreams
- Research phases I–VIII under `research/`
- Cost- and capacity-aware experiments (mean reversion, Almgren–Chriss, vol-target Kelly, multi-signal)
- Python package `medallion` with simulation utilities
- `make reproduce` pipeline
