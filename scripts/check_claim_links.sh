#!/usr/bin/env bash
# Fail if chapter/notebook pages use same-page-only claim anchors (broken cross-links).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITE="$ROOT/quarto/_site"

if [[ ! -d "$SITE" ]]; then
  echo "ERROR: $SITE not found; run quarto render first." >&2
  exit 1
fi

BAD=0
for dir in chapters notebooks; do
  if [[ ! -d "$SITE/$dir" ]]; then
    continue
  fi
  while IFS= read -r -d '' file; do
    if grep -q 'href="#claim-' "$file"; then
      echo "ERROR: bare claim fragment in $file (expected link to evidence registry)" >&2
      grep -n 'href="#claim-' "$file" >&2 | head -5 || true
      BAD=1
    fi
  done < <(find "$SITE/$dir" -name '*.html' -print0)
done

REGISTRY="$SITE/appendices/evidence-registry.html"
if [[ ! -f "$REGISTRY" ]]; then
  echo "ERROR: missing $REGISTRY" >&2
  exit 1
fi
if ! grep -q 'id="claim-CLM-2026-001"' "$REGISTRY"; then
  echo "ERROR: evidence registry missing claim anchor claim-CLM-2026-001" >&2
  exit 1
fi

if [[ "$BAD" -ne 0 ]]; then
  exit 1
fi

DATA="$SITE/chapters/02-data.html"
if [[ -f "$DATA" ]]; then
  if ! grep -q 'evidence-registry.html#claim-CLM-2027-001' "$DATA"; then
    echo "ERROR: chapters/02-data.html missing registry link for CLM-2027-001" >&2
    exit 1
  fi
  if ! grep -q 'class="claim-ref"' "$DATA"; then
    echo "ERROR: claim links missing claim-ref class (expected styled tooltip)" >&2
    exit 1
  fi
  if ! grep -q 'data-claim-tip="CRSP-style' "$DATA"; then
    echo "ERROR: claim links missing data-claim-tip tooltip text" >&2
    exit 1
  fi
  if grep -q 'edit/main/chapters/' "$DATA"; then
    echo "ERROR: Edit link missing repo-subdir quarto/ prefix" >&2
    exit 1
  fi
  if ! grep -q 'edit/main/quarto/chapters/02-data.qmd' "$DATA"; then
    echo "ERROR: Edit link should target quarto/chapters/02-data.qmd on GitHub" >&2
    exit 1
  fi
fi

echo "Claim link check passed (chapters/notebooks link to evidence registry)."
