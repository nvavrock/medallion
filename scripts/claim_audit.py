#!/usr/bin/env python3
"""Run evidence claim audit against research/ markdown."""

from __future__ import annotations

import sys

from medallion.evidence import audit_claims


def main() -> int:
    errors, warnings = audit_claims()
    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    if errors:
        print(f"\nClaim audit failed: {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Claim audit passed ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
