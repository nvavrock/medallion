#!/usr/bin/env python3
"""Lint research markdown against docs/evidence_rubric.md heuristics."""

from __future__ import annotations

import argparse
import sys

from medallion.rubric_lint import lint_research


def main() -> int:
    parser = argparse.ArgumentParser(description="Rubric lint for research/")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors (for CI after corpus is tuned)",
    )
    args = parser.parse_args()

    errors, warnings = lint_research()

    for w in warnings:
        print(f"WARNING [{w.rule}] {w.path}: {w.message}")
    for e in errors:
        print(f"ERROR [{e.rule}] {e.path}: {e.message}", file=sys.stderr)

    fail_warnings = args.strict and warnings
    if errors or fail_warnings:
        n_err = len(errors) + (len(warnings) if args.strict else 0)
        print(f"\nRubric lint failed: {n_err} issue(s).", file=sys.stderr)
        return 1

    print(f"Rubric lint passed ({len(warnings)} warning(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
