# Publishing the Quarto site

## Prerequisites

- [Quarto CLI](https://quarto.org/docs/get-started/) 1.4+
- Python environment: `make install`

## Local build (private repo phase)

```bash
make smoke          # generate experiment JSON for chapter 07
make site           # quarto-assets + claim-audit + quarto render
make preview        # live preview at http://localhost:4200
```

Output: `quarto/_site/` (gitignored). Open `quarto/_site/index.html` in a browser.

## Pipeline

1. `scripts/build_quarto_assets.py` — `references.bib`, appendices, `filters/claims-map.json`
2. `scripts/claim_audit.py` — validate research claim IDs
3. `quarto render quarto` — Lua filter resolves `[[claim:CLM-...]]`

## GitHub Pages (when repo is public)

1. Settings → General → change repository visibility to **Public**
2. Settings → Pages → Build and deployment → Source: **GitHub Actions**
3. Run workflow **Quarto Publish** (or push to `main` once triggers are enabled)
4. Site URL: **https://nvavrock.github.io/medallion/**

While the repo is private, the workflow runs on `workflow_dispatch` only; Pages will not serve until the repo is public.

## PDF export (optional)

```bash
cd quarto && quarto render --to pdf
```

## Dual license

See [disclaimer.md](disclaimer.md): MIT for code, CC BY-NC 4.0 for research and site content.
