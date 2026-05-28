# Methodology — matrix estimates {#methodology}

**Last updated:** 2026-05-26

How fields in [data_availability_matrix.yaml](data_availability_matrix.yaml) were estimated. This is **not** a reconstruction of Renaissance Technologies internal budgets or vendor contracts.

## Ordinal bands (not dollars)

| Field | Bands | Meaning |
|-------|-------|---------|
| `cost` | low / medium / high / very_high | Relative license + engineering burden for a systematic shop in the stated era |
| `storage_gb_per_year` | numeric order-of-magnitude | Compressed research store per year of history, not production tick retention |
| `compute` | desktop → gpu_cluster | Minimum plausible environment to **research** the dataset class |
| `viability` | high / medium / low / not_applicable | Overall usefulness for Medallion-era reconstruction |
| `predictive_viability` | prose | Why/when signals might work; ties to Phase III half-lives |

Industry norms for tape consolidation [[claim:CLM-2027-002]], L2 vendor eras [[claim:CLM-2027-003]], and alt-data timelines [[claim:CLM-2027-007]]–[[claim:CLM-2027-010]] anchor `earliest_year` where claims exist. Rows without dedicated claims use cross-cutting E1 hypotheses on data engineering [[claim:CLM-2027-014]].

## Evidence levels in this chapter

- **E2–E3:** Vendor documentation, market-structure summaries, academic microstructure (e.g. Hasbrouck), CRSP/WRDS guides.
- **E1:** RenTech-specific feed quality, cleaning, or early access—labeled explicitly in `medallion_era` and era narrative.

Every matrix row lists `claim_ids` that must resolve in `data/evidence.yaml` before prose cites the same fact.

## Validation

```bash
python scripts/validate_data_matrix.py
make claim-audit
```

The JSON Schema is [data_availability_row.schema.json](https://github.com/nvavrock/medallion/blob/main/schemas/data_availability_row.schema.json). Gate A requires named core asset classes and ≥6 alternative rows.

## What we do not claim

- Dollar-accurate data budgets or headcount for data engineering.
- That any single dataset was **the** source of Medallion returns.
- Point-in-time fundamentals without a paid point-in-time product (see [[claim:CLM-2027-012]] counterarguments).

Future Phase VII experiments must cite matrix rows before using alt-data in simulations (see Phase I bridge text in [strategy evolution](../chapters/01-history.html#strategy-evolution-map)).

## Maintenance

When adding a matrix row, update: (1) `claim_ids` in [data/evidence.yaml](https://github.com/nvavrock/medallion/blob/main/data/evidence.yaml) first, (2) `linked_signals` for affected SIG-* entries, (3) [signal → data crosswalk](#signal-data-map), and (4) re-run `python scripts/validate_data_matrix.py`. Regenerate the Quarto table with `make quarto-assets`.
