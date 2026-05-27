# Phase II — Data Architecture

**Last updated:** 2026-05-26

## Summary

Phase II documents **what data existed when** (1980–2025) for reconstructing a Medallion-like systematic shop: a claim-tagged [Historical Data Availability Matrix](data_availability_matrix.yaml), era narratives, traditional/alt deep dives, estimation methodology, and a **signal → dataset** crosswalk for Phase III and Phase VII.

## Reading order

1. [era_availability.md](era_availability.md) — 1980s / 1990s / 2000s / 2010s+  
2. [traditional_markets.md](traditional_markets.md) — EOD → tick → L2  
3. [alternative_data.md](alternative_data.md) — cost, latency, half-life  
4. [methodology.md](methodology.md) — ordinal bands and disclaimers  
5. [signal_data_map.md](signal_data_map.md) — all 15 signals mapped  
6. [data_availability_matrix.yaml](data_availability_matrix.yaml) — machine-readable inventory (28 rows)

## Evidence

Matrix rows cite `claim_ids` resolved in [data/evidence.yaml](../../data/evidence.yaml). Data-era claims are `CLM-2027-001` … `CLM-2027-018`. Prose uses `[[claim:CLM-...]]` anchors.

## Requirements satisfied

| ID | Deliverable |
|----|-------------|
| R2 | [data_availability_matrix.yaml](data_availability_matrix.yaml) |
| R2b | [era_availability.md](era_availability.md) |
| R2c | [traditional_markets.md](traditional_markets.md) + [alternative_data.md](alternative_data.md) |
| R2d | [signal_data_map.md](signal_data_map.md) |

## Review Gate A checklist

- [x] Core traditional: tick/trades, futures, FX, equities (daily + intraday path), corporate actions, order book, options, vol surfaces  
- [x] ≥6 alternative categories with era notes (weather, satellite, news/NLP, macro, geopolitical, shipping/flows, sentiment, transcripts, text corpora)  
- [x] ≥25 matrix rows with `predictive_viability` and `claim_ids`  
- [x] 15/15 signals in [signal_data_map.md](signal_data_map.md)  
- [x] Schema + validator: [schemas/data_availability_row.schema.json](../../schemas/data_availability_row.schema.json), [scripts/validate_data_matrix.py](../../scripts/validate_data_matrix.py)

## Links

- Phase I strategy eras: [strategy_evolution.md](../phase_01_history/strategy_evolution.md)  
- Phase III signals: [phase_03_signals/README.md](../phase_03_signals/README.md)  
- Quarto chapter: [quarto/chapters/02-data.qmd](../../quarto/chapters/02-data.qmd)

## How this chapter fits the reconstruction

Phase I established **when** strategies and personnel changed; Phase II establishes **what inputs could exist** in each era. Rows are conservative on RenTech-specific access: where public sources only document industry timelines, `medallion_era` strings label **E1** hypotheses explicitly. Phase III signal essays should cite both a signal ID and the matrix rows in [signal_data_map.md](signal_data_map.md) before claiming a data-dependent mechanism. Phase VII toy experiments must register external paths in [data/manifest.yaml](../../data/manifest.yaml) even when using public APIs (FRED, yfinance stubs)—so provenance stays auditable when the site is published.

## QA

```bash
python scripts/validate_data_matrix.py
make claim-audit
make site
```
