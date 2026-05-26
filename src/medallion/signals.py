"""Signal Hypothesis Database loader and validation."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import jsonschema
import yaml

from medallion.paths import SIGNALS_PATH, SCHEMAS_DIR


@dataclass(frozen=True)
class SignalHypothesis:
    signal_id: str
    signal: str
    theory: str
    evidence: str
    replication: str
    capacity: str
    confidence: float
    era_plausibility: str
    tags: list[str]
    evidence_level: str = "E2"
    failure_modes: str = ""
    alpha_half_life: str = ""
    status: str = "active"


def load_signal_schema() -> dict[str, Any]:
    return json.loads((SCHEMAS_DIR / "signal_hypothesis.schema.json").read_text())


def load_signals(path: Path | None = None) -> list[SignalHypothesis]:
    path = path or SIGNALS_PATH
    raw = yaml.safe_load(path.read_text())
    signals = raw.get("signals", [])
    schema = load_signal_schema()
    validator = jsonschema.Draft202012Validator(schema)
    out: list[SignalHypothesis] = []
    for item in signals:
        validator.validate(item)
        fields = {k: item[k] for k in item}
        out.append(SignalHypothesis(**fields))
    return out


def signals_by_tag(tag: str, path: Path | None = None) -> list[SignalHypothesis]:
    return [s for s in load_signals(path) if tag in s.tags]
