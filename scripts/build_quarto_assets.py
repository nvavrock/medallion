#!/usr/bin/env python3
"""Generate Quarto assets: references.bib, appendices, claims-map for Lua filter."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
QUARTO = ROOT / "quarto"
APPENDICES = QUARTO / "appendices"
FILTERS = QUARTO / "filters"


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def build_bib() -> None:
    bib = load_yaml(DATA / "bibliography.yaml")
    lines: list[str] = []
    for key, src in bib.get("sources", {}).items():
        author = src.get("author", "Unknown")
        title = src.get("title", key)
        year = src.get("year") or "n.d."
        note = src.get("note", "")
        stype = src.get("type", "misc")
        entry = "@book" if stype == "book" else "@article" if stype == "paper" else "@misc"
        lines.append(f"{entry}{{{key},")
        lines.append(f"  author = {{{author}}},")
        lines.append(f"  title = {{{title}}},")
        lines.append(f"  year = {{{year}}},")
        if note:
            lines.append(f"  note = {{{note}}},")
        lines.append("}")
        lines.append("")
    (QUARTO / "references.bib").write_text("\n".join(lines), encoding="utf-8")


def build_evidence_appendix() -> dict[str, dict]:
    raw = load_yaml(DATA / "evidence.yaml")
    claims = raw.get("claims", [])
    lines = ["# Evidence registry (generated)", ""]
    claims_map: dict[str, dict] = {}
    for c in claims:
        cid = c["claim_id"]
        claims_map[cid] = {
            "text": c["text"],
            "evidence_level": c["evidence_level"],
            "confidence": c["confidence"],
        }
        lines.append(f"### {cid} {{#claim-{cid}}}")
        lines.append("")
        lines.append(c["text"])
        lines.append("")
        lines.append(
            f"*Level:* {c['evidence_level']} | *Quality:* {c['source_quality']} | "
            f"*Replication:* {c['replication_status']} | *Confidence:* {c['confidence']}"
        )
        lines.append("")
        if c.get("sources"):
            lines.append(f"*Sources:* {', '.join(c['sources'])}")
            lines.append("")
        if c.get("counterarguments"):
            lines.append("*Counterarguments:*")
            for ca in c["counterarguments"]:
                lines.append(f"- {ca}")
            lines.append("")
    (APPENDICES / "_generated-evidence.md").write_text("\n".join(lines), encoding="utf-8")
    FILTERS.mkdir(parents=True, exist_ok=True)
    (FILTERS / "claims-map.json").write_text(json.dumps(claims_map, indent=2), encoding="utf-8")
    return claims_map


def build_signals_appendix() -> None:
    raw = load_yaml(DATA / "signals.yaml")
    signals = raw.get("signals", [])
    lines = [
        "# Signal hypothesis database (generated)",
        "",
        "| ID | Signal | Confidence | Era | Tags |",
        "|----|--------|------------|-----|------|",
    ]
    for s in signals:
        tags = ", ".join(s.get("tags", []))
        lines.append(
            f"| {s['signal_id']} | {s['signal']} | {s['confidence']} | "
            f"{s['era_plausibility']} | {tags} |"
        )
    lines.append("")
    for s in signals:
        lines.append(f"### {s['signal_id']} — {s['signal']}")
        lines.append("")
        lines.append(f"**Theory:** {s['theory']}")
        lines.append("")
        lines.append(f"**Evidence:** {s['evidence']}")
        lines.append("")
        lines.append(
            f"**Replication:** {s['replication']} | **Capacity:** {s['capacity']} | "
            f"**Confidence:** {s['confidence']}"
        )
        lines.append("")
        if s.get("failure_modes"):
            lines.append(f"**Failure modes:** {s['failure_modes']}")
            lines.append("")
    (APPENDICES / "_generated-signals.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    APPENDICES.mkdir(parents=True, exist_ok=True)
    build_bib()
    build_evidence_appendix()
    build_signals_appendix()
    print("Quarto assets written to quarto/")


if __name__ == "__main__":
    main()
