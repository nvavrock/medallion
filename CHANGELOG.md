# Changelog

## [Unreleased]

## [1.0.22] - 2026-05-29

### Changed

- **Logo:** replaced site branding with `rockstedy_logo_03.png` (navbar and hero pages)

## [1.0.21] - 2026-05-28

### Added

- **Chapter & appendix dividers:** 5px maroon rule under page titles before first section

### Changed

- **Home & About:** intro-style hero (logo, title band, tagline) matching Introduction page

## [1.0.20] - 2026-05-28

### Changed

- **Chapter naming:** page titles use `Chapter I–VIII`; sidebar section renamed to Chapters with compact labels (`I — Historical Reconstruction`, etc.)
- **Cross-links:** research corpus and site index/intro updated from Phase to Chapter references

## [1.0.19] - 2026-05-28

### Changed

- **Intro tagline:** larger font and horizontal position tuned for “Quantitative archaeology from public evidence only.”

## [1.0.18] - 2026-05-28

### Changed

- **Title position:** fine-tuned Medallion Fund Reconstruction placement (navbar + intro hero)

## [1.0.17] - 2026-05-28

### Added

- **Navbar subnav layout:** Home and About sit below the site title (desktop); intro hero tagline matches

### Changed

- **Title styling:** laptop-blue background on Medallion title (navbar + intro); tuned font size, vertical position, and compact band height
- **Intro hero:** tagline stacked under title with aligned positioning

## [1.0.16] - 2026-05-28

### Fixed

- **Brand title vertical align:** Medallion title sits above the rhino horn (navbar + intro hero); transparent overlap retained

## [1.0.15] - 2026-05-28

### Changed

- **Navbar title position:** Medallion title raised to ~75% up the logo; transparent overlap banner (no cream box)
- **Navigation:** Introduction moved from navbar to first item under Research in the sidebar

## [1.0.14] - 2026-05-28

### Fixed

- **Navbar title clip:** light cream banner overlaps the logo (UserForm-style) so the full **Medallion Fund Reconstruction** title is visible; intro hero matches

## [1.0.13] - 2026-05-28

### Added

- **Introduction page:** onboarding for new readers (project scope, evidence rubric, where to start)
- **Navbar branding:** larger logo, maroon overlapping site title

### Fixed

- **About page logo:** reliable `./images/` path and larger display (no tiny Pandoc figure)

## [1.0.12] - 2026-05-28

### Added

- **Rocksteady Analytics branding:** navbar logo, author credits on about/index/footer (Nate Vavrock)
- **Hasbrouck free PDF:** `hasbrouck2004_pdf` bibliography entry and callout on the bibliography appendix
- **Edit-link guard:** CI checks GitHub “Edit this page” URLs include the `quarto/` repo subdir

### Fixed

- **Edit this page 404:** `website.repo-subdir: quarto` so GitHub edit links target `quarto/chapters/*.qmd`

## [1.0.11] - 2026-05-29

### Added

- **Claim link tooltips:** hovering `[[claim:CLM-*]]` links shows the full evidence claim text in a styled popup (no need to open the registry for a quick read); click still opens the evidence registry

## [1.0.10] - 2026-05-29

### Fixed

- Bibliography callout no longer displays the obsolete `2019/05/13` Berkeley path (that text invited testing a URL that always 404s)
- CI fails if deployed bibliography HTML contains the broken Berkeley slug

## [1.0.9] - 2026-05-29

### Fixed

- Berkeley bibliography entry: italic article title is now a direct external link (not only the trailing URL)
- Bibliography appendix callout with canonical April 18, 2019 obituary link and hard-refresh note

## [1.0.8] - 2026-05-29

### Fixed

- Footnote Berkeley URL links on bibliography pages now include `rel="noopener noreferrer"` (avoids Cloudflare blocks from `github.io` referer)
- Live deploy verification: `verify_bibliography_urls.py` checks history chapter for external (not `#ref-`) Berkeley biblioref links

## [1.0.7] - 2026-05-29

### Fixed

- **In-text bibliography links:** `scripts/patch_bib_external_links.py` rewrites `(News, 2019)` and other web-source cites to open the external URL directly (not only `#ref-*` footnotes), so clicking the cite goes to Berkeley News instead of a same-page anchor

### Changed

- Runs after every `quarto render` (`make site`, CI, `check_quarto_warnings.sh`)

## [1.0.6] - 2026-05-29

### Fixed

- Bibliography appendix: no-cache meta headers to avoid stale cached HTML with the old Berkeley URL

### Added

- [`scripts/verify_bibliography_urls.py`](scripts/verify_bibliography_urls.py): validates YAML, `references.bib`, local `_site`, and live Pages for the Berkeley slug; wired into [`scripts/check_bibliography.sh`](scripts/check_bibliography.sh)

## [1.0.5] - 2026-05-29

### Fixed

- **Berkeley obituary URL:** `berkeley_news_berlekamp2019` in [`data/bibliography.yaml`](data/bibliography.yaml) now points to the live April 18, 2019 Berkeley News article (was a 404 with wrong date/slug)

## [1.0.4] - 2026-05-28

### Added

- **Bibliography appendix:** `nocite: @*` populates full reference list on [bibliography.qmd](quarto/appendices/bibliography.qmd)
- Pandoc citations `[@key]` in research prose and evidence registry sources
- [`scripts/validate_bibliography.py`](scripts/validate_bibliography.py), [`scripts/check_bibliography.sh`](scripts/check_bibliography.sh), [`schemas/bibliography_source.schema.json`](schemas/bibliography_source.schema.json)
- `url` fields on web/secondary bibliography entries; emitted in `references.bib`

### Changed

- Migrated legacy `[key]` → `[@key]` in Phase I history and Phase IV execution prose
- [`docs/evidence_rubric.md`](docs/evidence_rubric.md), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/qa_manual_checklist.md](docs/qa_manual_checklist.md)

## [1.0.3] - 2026-05-28

### Fixed

- Duplicate phase titles on site chapters II–IV, VII–VIII: removed redundant H1 from included research READMEs/synthesis (Quarto `.qmd` `title:` is the page heading)

## [1.0.2] - 2026-05-28

### Fixed

- **Claim ref links:** `[[claim:CLM-*]]` in chapters now link to [evidence registry](quarto/appendices/evidence-registry.qmd) (`../appendices/evidence-registry.html#claim-*`) instead of broken same-page `#claim-*` anchors
- Regression guard: [`scripts/check_claim_links.sh`](scripts/check_claim_links.sh) in `make quarto-check`

## [1.0.1] - 2026-05-28

### Added

- **`make qa`** and **`make qa-full`** — single entry for gates A–D (and A–E with site render)
- **PR CI** ([.github/workflows/ci.yml](.github/workflows/ci.yml)): `make reproduce` + `make quarto-check` without full Pages deploy
- **Validators:** `validate_experiment_contracts.py`, `validate_experiment_summaries.py`, `rubric_lint.py` (wired into `quarto-check`)
- **Live link check** ([.github/workflows/link-check.yml](.github/workflows/link-check.yml)) — weekly github.io crawl (non-blocking)
- [docs/qa_manual_checklist.md](docs/qa_manual_checklist.md), [scripts/sample_evidence.py](scripts/sample_evidence.py), [docs/qa_reports/2026-05-28.md](docs/qa_reports/2026-05-28.md)

### Changed

- [docs/test_plan.md](docs/test_plan.md), [README.md](README.md), [CONTRIBUTING.md](CONTRIBUTING.md), [docs/traceability.md](docs/traceability.md), [docs/publishing.md](docs/publishing.md) — QA workflow documented

## [1.0.0] - 2026-05-28

Charter-complete public reconstruction (Epics 2–5).

### Added

- **Epic 2:** `scripts/validate_evidence_coverage.py`; sensitivity sweeps in EXP-03/04/05 `summary.json`; [evidence_index.md](research/phase_08_synthesis/evidence_index.md)
- **Epic 3:** Phase IV–VI and VIII narrative depth (models, risk layers, org culture/workflow, experiment integration, failed peers)
- **Epic 4:** EXP-06 (VRP toy), EXP-08 (regime gate toy); manifest `optional` local data policy
- **Epic 5:** [CONTRIBUTING.md](CONTRIBUTING.md), [docs/traceability.md](docs/traceability.md), synthesis corpus map

### Changed

- Quarto chapters 04–08 multi-include structure; six experiments in `make smoke`
- Charter M2–M4 and SM1–SM6 status; requirements PDF table marked Done

## [0.6.0] - 2026-05-28

### Fixed

- Quarto cross-links on GitHub Pages: in-chapter `#` anchors (Phase II), `../chapters/*.html` and `../appendices/*.html` paths, GitHub blob URLs for repo source files
- Zero unresolved link warnings enforced by `scripts/check_quarto_warnings.sh` in `make quarto-check`

### Changed

- CI ([quarto-publish.yml](.github/workflows/quarto-publish.yml)) runs `make reproduce` before `make site`
- [docs/test_plan.md](docs/test_plan.md), [docs/charter.md](docs/charter.md), and [README.md](README.md) aligned with live Pages and Gate D pass

## [0.5.0] - 2026-05-28

### Added

- Phase III signal cluster essays: `core_stat_arb.md`, `options_vol.md`, `modern_ml.md`; Quarto chapter 03 includes full prose
- Gate B automation: `audit_gate_b()` in `medallion.signals`, `scripts/validate_signals.py`, wired into `make quarto-check`
- Expanded Phase IV–VI narratives (execution, risk stack, org matrix) and Phase VIII synthesis (ranges, counterarguments, explicit rejection of win-rate mantra)

### Changed

- Six signals (SIG-005, 008, 010, 011, 012, 014) upgraded from `not_attempted` to `partial` with documented replication limits
- GitHub Actions `quarto-publish.yml` runs on push to `main` (enable GitHub Pages when repository is public)
- [docs/test_plan.md](docs/test_plan.md) updated for v0.5.0 gates

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
