#!/usr/bin/env python3
"""Migrate legacy [bib_key] citations to Pandoc [@bib_key] in research markdown."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
BIB_PATH = ROOT / "data" / "bibliography.yaml"


def load_bib_keys() -> set[str]:
    raw = yaml.safe_load(BIB_PATH.read_text(encoding="utf-8"))
    return set(raw.get("sources", {}).keys())


def migrate_text(text: str, keys: set[str]) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        key = match.group(1)
        if key not in keys:
            return match.group(0)
        count += 1
        return f"[@{key}]"

    # [key] but not [text](url) or [@key] already
    pattern = re.compile(r"(?<!\@)\[(" + "|".join(re.escape(k) for k in sorted(keys, key=len, reverse=True)) + r")\]")
    new_text = pattern.sub(repl, text)
    return new_text, count


def main() -> int:
    keys = load_bib_keys()
    total = 0
    for path in sorted(RESEARCH.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        updated, n = migrate_text(original, keys)
        if n:
            path.write_text(updated, encoding="utf-8")
            print(f"{path.relative_to(ROOT)}: {n} citation(s)")
            total += n
    print(f"Migrated {total} citation(s) total.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
