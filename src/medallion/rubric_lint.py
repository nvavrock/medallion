"""Heuristic rubric checks for research markdown (see docs/evidence_rubric.md)."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from medallion.evidence import CLAIM_REF_PATTERN, evidence_by_id
from medallion.paths import RESEARCH_DIR

HEDGE_WORDS = re.compile(
    r"\b(hypothesi[sz]e|hypothesis|speculative|inference|inferred|band|range|"
    r"may|might|could|suggest|reported|public accounts|not used|does not prove|"
    r"toy|toys|directional|narrative|secondary sources)\b",
    re.IGNORECASE,
)

WIN_RATE_PATTERN = re.compile(r"\b(win rate|hit rate)\b", re.IGNORECASE)
WIN_RATE_ALLOW = re.compile(
    r"\b(not used|do not use|avoid|without new supporting|anecdotes vary)\b",
    re.IGNORECASE,
)

OVERCLAIM_VERB = re.compile(r"\b(proves?|replicates?|confirms?)\b", re.IGNORECASE)
MEDALLION = re.compile(r"\bMedallion\b", re.IGNORECASE)

PERF_NUMBER = re.compile(
    r"(\d+(\.\d+)?\s*[×x]\s*\d|Sharpe\s*[><=~]?\s*\d|>\s*\d+\s*Sharpe)",
    re.IGNORECASE,
)

E1_FACT_PATTERN = re.compile(
    r"\b(is|was|are|were|returns?|operated|uses?)\b[^.\n]{0,80}\[\[claim:(CLM-[^]]+)\]\]",
    re.IGNORECASE,
)

POINT_SHARPE = re.compile(
    r"\bSharpe\b[^.\n]{0,40}\b(\d+(\.\d+)?)\b",
    re.IGNORECASE,
)
SHARPE_BAND_CONTEXT = re.compile(
    r"\b(band|range|~|speculative|hypothesis|>\s*\d|3–7|3-7|not audited|toy)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class LintFinding:
    severity: str  # "error" | "warning"
    path: str
    rule: str
    message: str


def _paragraphs(text: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def _has_claim_near(text: str, window: str) -> bool:
    return bool(CLAIM_REF_PATTERN.search(text)) or bool(CLAIM_REF_PATTERN.search(window))


def lint_file(path: Path, db: dict | None = None) -> list[LintFinding]:
    if db is None:
        db = evidence_by_id()

    try:
        rel = str(path.relative_to(RESEARCH_DIR.parent))
    except ValueError:
        rel = str(path)
    text = path.read_text(encoding="utf-8")
    findings: list[LintFinding] = []

    # experiment_integration.md: "Proves (directional)" table is intentional
    is_exp_integration = path.name == "experiment_integration.md"

    for line_no, line in enumerate(text.splitlines(), start=1):
        if WIN_RATE_PATTERN.search(line) and not WIN_RATE_ALLOW.search(line):
            findings.append(
                LintFinding(
                    "error",
                    rel,
                    "forbidden_metric",
                    f"line {line_no}: win/hit rate cited without disclaimer",
                )
            )

    for para in _paragraphs(text):
        if not para or para.startswith("|") and para.count("|") > 2:
            # table rows handled separately where needed
            pass

        if OVERCLAIM_VERB.search(para) and MEDALLION.search(para):
            if is_exp_integration and (
                "does not prove" in para.lower()
                or para.lstrip().startswith("| EXP-")
                or re.search(r"\bNone\b.*\breplicate", para, re.IGNORECASE)
            ):
                continue
            if "**Replication:**" in para or re.search(r"\bno Medallion\b", para, re.IGNORECASE):
                continue
            if not HEDGE_WORDS.search(para):
                findings.append(
                    LintFinding(
                        "warning",
                        rel,
                        "overclaim_medallion",
                        f"strong verb + Medallion without hedge: {para[:120]}...",
                    )
                )

        if PERF_NUMBER.search(para) and not _has_claim_near(para, ""):
            if HEDGE_WORDS.search(para):
                continue
            findings.append(
                LintFinding(
                    "warning",
                    rel,
                    "perf_without_cite",
                    f"performance number without [[claim:]]: {para[:120]}...",
                )
            )

        for m in E1_FACT_PATTERN.finditer(para):
            claim_id = m.group(1)
            rec = db.get(claim_id)
            if rec and rec.evidence_level == "E1" and not HEDGE_WORDS.search(para):
                findings.append(
                    LintFinding(
                        "warning",
                        rel,
                        "e1_as_fact",
                        f"E1 claim {claim_id} in assertive prose without hedge",
                    )
                )

        if POINT_SHARPE.search(para) and not SHARPE_BAND_CONTEXT.search(para):
            if CLAIM_REF_PATTERN.search(para):
                continue
            findings.append(
                LintFinding(
                    "warning",
                    rel,
                    "point_sharpe",
                    f"Sharpe point value without band/range context: {para[:120]}...",
                )
            )

    return findings


def lint_research(research_dir: Path | None = None) -> tuple[list[LintFinding], list[LintFinding]]:
    research_dir = research_dir or RESEARCH_DIR
    db = evidence_by_id()
    errors: list[LintFinding] = []
    warnings: list[LintFinding] = []

    for path in sorted(research_dir.rglob("*.md")):
        if "_generated" in path.parts:
            continue
        for finding in lint_file(path, db):
            if finding.severity == "error":
                errors.append(finding)
            else:
                warnings.append(finding)

    return errors, warnings
