#!/usr/bin/env python3
"""Validate signals.yaml schema and review Gate B."""

from __future__ import annotations

import sys

from medallion.signals import audit_gate_b, load_signals


def main() -> int:
    load_signals()
    errors = audit_gate_b()
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    if errors:
        print(f"\nSignal validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1
    print("Signal validation passed (Gate B).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
