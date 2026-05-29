#!/usr/bin/env bash
# Fail if bibliography appendix is empty or chapter citations did not render.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITE="$ROOT/quarto/_site"

if [[ ! -d "$SITE" ]]; then
  echo "ERROR: $SITE not found; run quarto render first." >&2
  exit 1
fi

BIB="$SITE/appendices/bibliography.html"
HIST="$SITE/chapters/01-history.html"

if [[ ! -f "$BIB" ]]; then
  echo "ERROR: missing $BIB" >&2
  exit 1
fi

if ! grep -q 'class="csl-entry"' "$BIB" && ! grep -q 'id="ref-' "$BIB"; then
  echo "ERROR: bibliography appendix has no rendered references" >&2
  exit 1
fi

if [[ -f "$HIST" ]]; then
  if ! grep -q 'role="doc-biblioref"' "$HIST"; then
    echo "ERROR: chapters/01-history.html has no Pandoc biblioref links" >&2
    exit 1
  fi
  if grep -q 'href="#ref-berkeley_news_berlekamp2019" role="doc-biblioref"' "$HIST"; then
    echo "ERROR: berkeley in-text cite still uses internal #ref anchor (run patch_bib_external_links.py)" >&2
    exit 1
  fi
  if ! grep -q 'news.berkeley.edu/2019/04/18/elwyn-berlekamp' "$HIST"; then
    echo "ERROR: history chapter missing external Berkeley biblioref link" >&2
    exit 1
  fi
  if grep -q '\[zuckerman2019\]' "$HIST"; then
    echo "ERROR: legacy [zuckerman2019] still in history chapter HTML" >&2
    exit 1
  fi
fi

BROKEN_SLUG="2019/05/13/elwyn-b-j-berlekamp"
if grep -rq "$BROKEN_SLUG" "$SITE"; then
  echo "ERROR: broken Berkeley URL ($BROKEN_SLUG) found in quarto/_site HTML" >&2
  grep -rl "$BROKEN_SLUG" "$SITE" >&2
  exit 1
fi

"$ROOT/.venv/bin/python" "$ROOT/scripts/verify_bibliography_urls.py"

echo "Bibliography check passed (appendix populated, in-text cites linked)."
