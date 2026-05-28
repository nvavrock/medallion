#!/usr/bin/env python3
"""Ensure active evidence claims are cited in research/ or quarto/."""

from __future__ import annotations

import sys
from pathlib import Path

from medallion.evidence import CLAIM_REF_PATTERN, evidence_by_id, load_evidence

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [ROOT / "research", ROOT / "quarto"]


def collect_refs() -> set[str]:
    refs: set[str] = set()
    for base in SCAN_DIRS:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if path.suffix not in {".md", ".qmd"}:
                continue
            if "_site" in path.parts or ".quarto" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            refs.update(CLAIM_REF_PATTERN.findall(text))
    return refs


def main() -> int:
    load_evidence()
    db = evidence_by_id()
    refs = collect_refs()
    orphans = [
        cid
        for cid, rec in db.items()
        if rec.status == "active" and cid not in refs
    ]
    if orphans:
        for cid in sorted(orphans):
            print(f"ERROR: Active claim {cid} not cited in research/ or quarto/", file=sys.stderr)
        print(f"\nEvidence coverage failed: {len(orphans)} orphan(s).", file=sys.stderr)
        return 1
    print(f"Evidence coverage passed ({len(refs)} claim refs in corpus).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
