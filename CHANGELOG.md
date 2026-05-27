# Changelog

## [0.4.0] - 2026-05-26

### Added

- Phase II data architecture chapter: 28-row [data_availability_matrix.yaml](research/phase_02_data/data_availability_matrix.yaml) with `predictive_viability`, `medallion_era`, `claim_ids`, and `linked_signals`
- JSON Schema [schemas/data_availability_row.schema.json](schemas/data_availability_row.schema.json) and [scripts/validate_data_matrix.py](scripts/validate_data_matrix.py) (Gate A checks in `make quarto-check`)
- Eighteen data-era evidence records (CLM-2027-001–018); bibliography keys for CRSP, WRDS, SEC market structure, and alt-data surveys
- Narrative deliverables: `era_availability.md`, `traditional_markets.md`, `alternative_data.md`, `methodology.md`, `signal_data_map.md` (15/15 signals)
- Generated Quarto appendix `_generated-data-matrix.md`; manifest stubs for FRED and yfinance paths

### Changed

- [quarto/chapters/02-data.qmd](quarto/chapters/02-data.qmd) includes full Phase II prose; raw YAML dump removed
- Phase III README links to `signal_data_map.md`

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
