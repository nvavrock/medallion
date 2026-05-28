#!/usr/bin/env python3
"""Print a reproducible random sample of evidence claim IDs for manual QA."""

from __future__ import annotations

import argparse
import random
import sys

from medallion.evidence import load_evidence


def main() -> int:
    parser = argparse.ArgumentParser(description="Sample claim IDs from data/evidence.yaml")
    parser.add_argument("-n", "--count", "--n", type=int, default=8, dest="count", help="Number of claims to sample")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed for reproducibility")
    args = parser.parse_args()

    records = [r for r in load_evidence() if r.status == "active"]
    if not records:
        print("No active claims found.", file=sys.stderr)
        return 1

    n = min(args.count, len(records))
    rng = random.Random(args.seed)
    sample = sorted(rng.sample(records, n), key=lambda r: r.claim_id)

    print(f"# Sample (n={n}, seed={args.seed}) — verify level, sources, and prose tone\n")
    for rec in sample:
        src = ", ".join(rec.sources[:3])
        if len(rec.sources) > 3:
            src += ", ..."
        print(f"{rec.claim_id}\t{rec.evidence_level}\t{src}")
        print(f"  {rec.text[:100]}{'...' if len(rec.text) > 100 else ''}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
