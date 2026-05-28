#!/usr/bin/env python3
"""Validate experiments/*/contract.yaml against JSON schema and directory naming."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml

from medallion.paths import EXPERIMENTS_DIR, SCHEMAS_DIR

EXP_DIR_PATTERN = re.compile(r"^(\d{2})_")


def load_contract_schema() -> dict:
    return json.loads((SCHEMAS_DIR / "experiment_contract.schema.json").read_text())


def expected_exp_id(dir_name: str) -> str | None:
    m = EXP_DIR_PATTERN.match(dir_name)
    if not m:
        return None
    return f"EXP-{m.group(1)}"


def main() -> int:
    schema = load_contract_schema()
    validator = jsonschema.Draft202012Validator(schema)
    errors: list[str] = []

    contracts = sorted(EXPERIMENTS_DIR.glob("*/contract.yaml"))
    if not contracts:
        print("ERROR: No experiment contracts found.", file=sys.stderr)
        return 1

    for path in contracts:
        exp_dir = path.parent.name
        expected = expected_exp_id(exp_dir)
        if expected is None:
            errors.append(f"{path}: directory name must match NN_slug (got {exp_dir})")
            continue

        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        try:
            validator.validate(raw)
        except jsonschema.ValidationError as exc:
            errors.append(f"{path}: schema validation failed: {exc.message}")
            continue

        exp_id = raw.get("experiment_id", "")
        if exp_id != expected:
            errors.append(
                f"{path}: experiment_id {exp_id!r} does not match directory "
                f"(expected {expected})"
            )

    if errors:
        for msg in errors:
            print(f"ERROR: {msg}", file=sys.stderr)
        print(f"\nExperiment contract validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1

    print(f"Experiment contracts passed ({len(contracts)} file(s)).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
