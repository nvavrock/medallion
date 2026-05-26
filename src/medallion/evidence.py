"""Evidence record loading, validation, and claim-reference utilities."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import jsonschema
import yaml

from medallion.paths import EVIDENCE_PATH, RESEARCH_DIR, SCHEMAS_DIR

CLAIM_REF_PATTERN = re.compile(r"\[\[claim:(CLM-[0-9]{4}-[0-9]{3,})\]\]")


@dataclass(frozen=True)
class EvidenceRecord:
    claim_id: str
    text: str
    evidence_level: str
    source_quality: str
    sources: list[str]
    replication_status: str
    counterarguments: list[str]
    confidence: float
    last_verified: str
    status: str = "active"


def load_evidence_schema() -> dict[str, Any]:
    import json

    return json.loads((SCHEMAS_DIR / "evidence_record.schema.json").read_text())


def load_evidence(path: Path | None = None) -> list[EvidenceRecord]:
    path = path or EVIDENCE_PATH
    raw = yaml.safe_load(path.read_text())
    claims = raw.get("claims", [])
    schema = load_evidence_schema()
    validator = jsonschema.Draft202012Validator(schema)
    records: list[EvidenceRecord] = []
    for item in claims:
        validator.validate(item)
        records.append(
            EvidenceRecord(
                claim_id=item["claim_id"],
                text=item["text"],
                evidence_level=item["evidence_level"],
                source_quality=item["source_quality"],
                sources=item["sources"],
                replication_status=item["replication_status"],
                counterarguments=item["counterarguments"],
                confidence=item["confidence"],
                last_verified=item["last_verified"],
                status=item.get("status", "active"),
            )
        )
    return records


def evidence_by_id(path: Path | None = None) -> dict[str, EvidenceRecord]:
    return {r.claim_id: r for r in load_evidence(path)}


def find_claim_refs_in_text(text: str) -> list[str]:
    return CLAIM_REF_PATTERN.findall(text)


def scan_research_claim_refs(research_dir: Path | None = None) -> dict[str, list[str]]:
    """Map claim_id -> list of markdown files referencing it."""
    research_dir = research_dir or RESEARCH_DIR
    refs: dict[str, list[str]] = {}
    for md in research_dir.rglob("*.md"):
        content = md.read_text(encoding="utf-8")
        for claim_id in find_claim_refs_in_text(content):
            refs.setdefault(claim_id, []).append(str(md.relative_to(research_dir.parent)))
    return refs


def audit_claims(
    evidence_path: Path | None = None,
    research_dir: Path | None = None,
) -> tuple[list[str], list[str]]:
    """
    Returns (errors, warnings).
    Errors: referenced claims missing from DB, or E0 active claims.
    Warnings: DB claims never referenced in research.
    """
    errors: list[str] = []
    warnings: list[str] = []

    db = evidence_by_id(evidence_path)
    refs = scan_research_claim_refs(research_dir)

    for claim_id, files in refs.items():
        if claim_id not in db:
            errors.append(f"Missing evidence record for {claim_id} (cited in {', '.join(files)})")
        elif db[claim_id].evidence_level == "E0" and db[claim_id].status == "active":
            errors.append(f"Active E0 claim {claim_id} must not be cited as fact")

    for claim_id, rec in db.items():
        if rec.status == "active" and claim_id not in refs:
            warnings.append(f"Claim {claim_id} not referenced in research/")

    return errors, warnings
