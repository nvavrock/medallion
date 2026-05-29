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
  if grep -q '\[zuckerman2019\]' "$HIST"; then
    echo "ERROR: legacy [zuckerman2019] still in history chapter HTML" >&2
    exit 1
  fi
fi

echo "Bibliography check passed (appendix populated, in-text cites linked)."
