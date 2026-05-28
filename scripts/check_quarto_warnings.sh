#!/usr/bin/env bash
# Fail if Quarto render emits unresolved internal link warnings.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
QUARTO="${QUARTO:-$(command -v quarto 2>/dev/null || true)}"
if [[ -z "$QUARTO" || ! -x "$QUARTO" ]]; then
  echo "SKIP: Quarto not installed; link check deferred."
  exit 0
fi
LOG="$(mktemp)"
trap 'rm -f "$LOG"' EXIT
make quarto-assets >/dev/null
make smoke >/dev/null
cd quarto && "$QUARTO" render 2>&1 | tee "$LOG"
COUNT=$(grep -c "Unable to resolve link target" "$LOG" || true)
if [[ "$COUNT" -gt 0 ]]; then
  echo "ERROR: $COUNT unresolved Quarto link(s)." >&2
  grep "Unable to resolve link target" "$LOG" >&2 || true
  exit 1
fi
echo "Quarto link check passed (0 unresolved links)."
