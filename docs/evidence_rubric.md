# Evidence Rubric

Every assertive conclusion in research markdown or synthesis must map to an evidence record (see `schemas/evidence_record.schema.json`) or be rewritten as clearly speculative inline text.

## Required Fields (per claim)

| Field | Description |
|-------|-------------|
| `claim_id` | Stable ID, e.g. `CLM-2024-001` |
| `text` | The claim statement |
| `evidence_level` | E0–E4 (see below) |
| `source_quality` | S0–S3 (see below) |
| `sources` | Bibliography keys or URLs |
| `replication_status` | `not_attempted`, `failed`, `partial`, `replicated` |
| `counterarguments` | List of objections or alternative explanations |
| `confidence` | 0.0–1.0 subjective confidence |
| `last_verified` | ISO date |

## Evidence Levels

| Level | Label | Meaning |
|-------|-------|---------|
| E0 | Unsupported | No acceptable source; must not appear as fact |
| E1 | Anecdote / inference | Industry lore, logical inference from partial facts |
| E2 | Secondary summary | Journalism, interviews, textbooks citing others |
| E3 | Primary public | SEC filings, fund letters where public, peer-reviewed papers |
| E4 | Replicated | E3 plus independent replication in this repo or literature |

## Source Quality

| Score | Label | Examples |
|-------|-------|----------|
| S0 | Unreliable | Anonymous forums, unsourced blogs |
| S1 | Weak | Single anecdote, marketing material |
| S2 | Moderate | Reputable journalism (Zuckerman), practitioner essays |
| S3 | Strong | Academic papers, regulatory filings, replicated datasets |

## Language Rules

| Situation | Required phrasing |
|-----------|-------------------|
| E0–E1 | “We hypothesize…”, “One inference is…” |
| E2 | “Public accounts suggest…”, “Sources report…” |
| E3–E4 | “Evidence indicates…”, “Replication supports…” |

Avoid repeating “51% win rate × thousands of trades” without new supporting analysis.

## Performance Metrics (PDF review)

| Metric | Rule |
|--------|------|
| Leverage | State as **range** (e.g., 5×–12×), not a single point, unless E3 source gives a point |
| Sharpe | Report as **lower bound or band**; label exact values (e.g., 7–10) as speculative unless E3 |
| Kelly / HMM / etc. | Require E2+ or label E1 hypothesis |

## Citation Format

- Use bibliography keys in `data/bibliography.yaml` (e.g., `[zuckerman2019]`)
- Do **not** embed messy `#:~:text` URL fragments in prose
- Full URLs only in bibliography entries

## Claim Audit (QA)

The `scripts/claim_audit.py` tool flags:

- `[[claim:CLM-...]]` references missing from `data/evidence.yaml`
- Orphan evidence IDs never cited

Research files should cite claims as: `[[claim:CLM-2024-001]]`

## Replication Status

| Status | When to use |
|--------|-------------|
| `not_attempted` | No experiment or literature check yet |
| `failed` | Attempted; does not support claim |
| `partial` | Directionally supports under narrow assumptions |
| `replicated` | Experiment or cited paper reproduces core effect |
