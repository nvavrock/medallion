# Phase I — Historical Reconstruction

**Last updated:** 2026-05-26

## Summary

Phase I reconstructs the **public** arc of Monemetrics / Renaissance Technologies and the Medallion Fund: founding, early crises, Berlekamp overhaul, employee-only structure, IBM hires, and succession—without claiming proprietary detail.

## Reading order

1. [timeline.md](timeline.md) — master chronology and era narratives  
2. [strategy_evolution.md](strategy_evolution.md) — strategy eras with Phase II data cross-links  
3. [personnel_matrix.md](personnel_matrix.md) — people, periods, mini-bios  
4. [infrastructure_timeline.md](infrastructure_timeline.md) — compute/data/execution context  

## Evidence

Major factual rows cite `[[claim:CLM-...]]` anchors stored in [data/evidence.yaml](../../data/evidence.yaml). The rendered **Evidence registry** lives in the Quarto site under *Appendices* (build with `make site`).

## Requirements satisfied

| ID | Deliverable |
|----|-------------|
| R1 | [timeline.md](timeline.md) |
| R1b | [strategy_evolution.md](strategy_evolution.md) |
| R1c | [personnel_matrix.md](personnel_matrix.md) |
| R1d | [infrastructure_timeline.md](infrastructure_timeline.md) |

## QA

```bash
make claim-audit
make site
```
