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

## GitHub Pages

**Live site:** https://nvavrock.github.io/medallion/

### One-time setup (required or you get a 404)

GitHub does **not** publish anything until Pages is enabled **and** at least one **Quarto Publish** workflow run succeeds.

1. Repository must be **Public** (or GitHub Enterprise Pages policy).
2. **Settings → Pages → Build and deployment → Source:** **GitHub Actions** (not “Deploy from a branch”).
3. Run the workflow once: **Actions → Quarto Publish → Run workflow**, or push to `main` (workflow triggers on push).

CLI equivalent (maintainers):

```bash
gh api -X POST repos/nvavrock/medallion/pages -f build_type=workflow
gh workflow run quarto-publish.yml -R nvavrock/medallion
```

### Ongoing deploys

The workflow runs on **push to `main`** and on **workflow_dispatch**. Deploy job uses the `github-pages` environment.

### Troubleshooting 404

| Symptom | Likely cause |
|---------|----------------|
| `github.io/medallion/` returns GitHub 404 | Pages never enabled, or no successful deploy yet |
| Workflow green but still 404 | Pages source still “branch” instead of Actions |
| Stale content | Wait ~1 min for CDN; hard-refresh |

Check: `gh api repos/nvavrock/medallion/pages` should return `html_url`, not 404.

## PDF export (optional)

```bash
cd quarto && quarto render --to pdf
```

## Dual license

See [disclaimer.md](disclaimer.md): MIT for code, CC BY-NC 4.0 for research and site content.
