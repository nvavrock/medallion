#!/usr/bin/env python3
"""Validate data_availability_matrix.yaml against schema and evidence DB."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema
import yaml

ROOT = Path(__file__).resolve().parents[1]
MATRIX_PATH = ROOT / "research" / "phase_02_data" / "data_availability_matrix.yaml"
SCHEMA_PATH = ROOT / "schemas" / "data_availability_row.schema.json"
EVIDENCE_PATH = ROOT / "data" / "evidence.yaml"
SIGNALS_PATH = ROOT / "data" / "signals.yaml"

GATE_A_CORE = {
    "equity_tick_trades",
    "equity_daily_ohlcv",
    "futures_continuous",
    "fx_spot_tick",
    "order_book_l2",
    "options_chain_eod",
    "volatility_surfaces",
    "corporate_actions",
    "news_wire_archives",
    "earnings_transcripts",
    "weather_gridded",
    "satellite_imagery",
    "shipping_ais",
    "economic_releases",
    "sentiment_scores",
    "geopolitical_events_structured",
    "commodity_flows_freight",
}


def main() -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    raw = yaml.safe_load(MATRIX_PATH.read_text(encoding="utf-8"))
    datasets = raw.get("datasets", [])
    evidence_ids = {
        c["claim_id"]
        for c in yaml.safe_load(EVIDENCE_PATH.read_text(encoding="utf-8")).get("claims", [])
    }
    signal_ids = {
        s["signal_id"]
        for s in yaml.safe_load(SIGNALS_PATH.read_text(encoding="utf-8")).get("signals", [])
    }
    errors: list[str] = []
    names: set[str] = set()

    if len(datasets) < 25:
        errors.append(f"Expected at least 25 dataset rows, got {len(datasets)}")

    for i, row in enumerate(datasets):
        try:
            validator.validate(row)
        except jsonschema.ValidationError as e:
            errors.append(f"Row {i} ({row.get('name', '?')}): {e.message}")
        name = row.get("name")
        if name in names:
            errors.append(f"Duplicate dataset name: {name}")
        names.add(name)
        for cid in row.get("claim_ids", []):
            if cid not in evidence_ids:
                errors.append(f"{name}: unknown claim_id {cid}")
        for sid in row.get("linked_signals", []):
            if sid not in signal_ids:
                errors.append(f"{name}: unknown linked_signal {sid}")

    missing = GATE_A_CORE - names
    if missing:
        errors.append(f"Gate A missing core rows: {sorted(missing)}")

    alt_count = sum(1 for d in datasets if d.get("category") == "alternative")
    if alt_count < 6:
        errors.append(f"Gate A needs >=6 alternative rows, got {alt_count}")

    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    if errors:
        print(f"\nData matrix validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"Data matrix validation passed ({len(datasets)} rows, {alt_count} alternative).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
