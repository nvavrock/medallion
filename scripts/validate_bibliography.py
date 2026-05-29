#!/usr/bin/env python3
"""Validate bibliography keys and Pandoc citation syntax in research/."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
BIB_PATH = ROOT / "data" / "bibliography.yaml"
EVIDENCE_PATH = ROOT / "data" / "evidence.yaml"
RESEARCH = ROOT / "research"
SCHEMA_PATH = ROOT / "schemas" / "bibliography_source.schema.json"


def load_bib_keys() -> set[str]:
    raw = yaml.safe_load(BIB_PATH.read_text(encoding="utf-8"))
    return set(raw.get("sources", {}).keys())


def validate_bib_schema() -> list[str]:
    errors: list[str] = []
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    raw = yaml.safe_load(BIB_PATH.read_text(encoding="utf-8"))
    for key, item in raw.get("sources", {}).items():
        try:
            validator.validate(item)
        except jsonschema.ValidationError as exc:
            errors.append(f"bibliography.yaml {key}: {exc.message}")
    return errors


def evidence_source_keys() -> set[str]:
    raw = yaml.safe_load(EVIDENCE_PATH.read_text(encoding="utf-8"))
    keys: set[str] = set()
    for claim in raw.get("claims", []):
        keys.update(claim.get("sources", []))
    return keys


def main() -> int:
    errors: list[str] = []
    errors.extend(validate_bib_schema())

    bib_keys = load_bib_keys()
    ev_keys = evidence_source_keys()
    missing = ev_keys - bib_keys
    if missing:
        for key in sorted(missing):
            errors.append(f"evidence.yaml references missing bibliography key: {key}")

    legacy_pattern = re.compile(
        r"(?<!\@)\[(" + "|".join(re.escape(k) for k in sorted(bib_keys, key=len, reverse=True)) + r")\]"
    )
    cite_pattern = re.compile(r"\[@([a-z][a-z0-9_]*)\]")

    for path in sorted(RESEARCH.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for m in legacy_pattern.finditer(text):
            errors.append(f"{rel}: legacy citation [{m.group(1)}] — use [@{m.group(1)}]")
        for m in cite_pattern.finditer(text):
            key = m.group(1)
            if key not in bib_keys:
                errors.append(f"{rel}: unknown citation [@{key}]")

    if errors:
        for msg in errors:
            print(f"ERROR: {msg}", file=sys.stderr)
        print(f"\nBibliography validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(
        f"Bibliography validation passed ({len(bib_keys)} sources, "
        f"{len(ev_keys)} evidence keys)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
