## Overview {#phase-ii-overview}

**Last updated:** 2026-05-28

## Summary

Chapter II documents **what data existed when** (1980–2025) for reconstructing a Medallion-like systematic shop: a claim-tagged [Historical Data Availability Matrix](https://github.com/nvavrock/medallion/blob/main/research/phase_02_data/data_availability_matrix.yaml), era narratives, traditional/alt deep dives, estimation methodology, and a **signal → dataset** crosswalk for Chapter III and Chapter VII.

## Reading order

1. [Era availability](#era-availability) — 1980s / 1990s / 2000s / 2010s+  
2. [Traditional markets](#traditional-markets) — EOD → tick → L2  
3. [Alternative data](#alternative-data) — cost, latency, half-life  
4. [Methodology](#methodology) — ordinal bands and disclaimers  
5. [Signal → data crosswalk](#signal-data-map) — all 15 signals mapped  
6. [data_availability_matrix.yaml](https://github.com/nvavrock/medallion/blob/main/research/phase_02_data/data_availability_matrix.yaml) — machine-readable inventory (28 rows)

## Evidence

Matrix rows cite `claim_ids` resolved in [data/evidence.yaml](https://github.com/nvavrock/medallion/blob/main/data/evidence.yaml). Data-era claims are `CLM-2027-001` … `CLM-2027-018`. Prose uses `[[claim:CLM-...]]` anchors.

## Requirements satisfied

| ID | Deliverable |
|----|-------------|
| R2 | [data_availability_matrix.yaml](https://github.com/nvavrock/medallion/blob/main/research/phase_02_data/data_availability_matrix.yaml) |
| R2b | [Era availability](#era-availability) |
| R2c | [Traditional markets](#traditional-markets) + [Alternative data](#alternative-data) |
| R2d | [Signal → data crosswalk](#signal-data-map) |

## Review Gate A checklist

- [x] Core traditional: tick/trades, futures, FX, equities (daily + intraday path), corporate actions, order book, options, vol surfaces  
- [x] ≥6 alternative categories with era notes (weather, satellite, news/NLP, macro, geopolitical, shipping/flows, sentiment, transcripts, text corpora)  
- [x] ≥25 matrix rows with `predictive_viability` and `claim_ids`  
- [x] 15/15 signals in [signal → data crosswalk](#signal-data-map)  
- [x] Schema + validator: [data_availability_row.schema.json](https://github.com/nvavrock/medallion/blob/main/schemas/data_availability_row.schema.json), [validate_data_matrix.py](https://github.com/nvavrock/medallion/blob/main/scripts/validate_data_matrix.py)

## Links

- Chapter I strategy eras: [Chapter I — History](../chapters/01-history.html#strategy-evolution-map)  
- Chapter III signals: [Chapter III — Signals](../chapters/03-signals.html)  
- This chapter on the site: [Chapter II — Data](../chapters/02-data.html)

## How this chapter fits the reconstruction

Chapter I established **when** strategies and personnel changed; Chapter II establishes **what inputs could exist** in each era. Rows are conservative on RenTech-specific access: where public sources only document industry timelines, `medallion_era` strings label **E1** hypotheses explicitly. Chapter III signal essays should cite both a signal ID and the matrix rows in the [signal → data crosswalk](#signal-data-map) before claiming a data-dependent mechanism. Chapter VII toy experiments must register external paths in [data/manifest.yaml](https://github.com/nvavrock/medallion/blob/main/data/manifest.yaml) even when using public APIs (FRED, yfinance stubs)—so provenance stays auditable when the site is published.

## QA

```bash
python scripts/validate_data_matrix.py
make claim-audit
make site
```
