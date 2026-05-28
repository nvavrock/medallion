# Research workflow (inferred) {#research-workflow}

**Last updated:** 2026-05-28

```mermaid
flowchart LR
  hypothesis[Hypothesis] --> data_acq[Data_acquisition]
  data_acq --> features[Feature_engineering]
  features --> models[Model_estimation]
  models --> portfolio[Portfolio_construction]
  portfolio --> execution[Execution]
  execution --> risk_monitor[Risk_monitoring]
  risk_monitor --> hypothesis
```

## Stages (E1–E2 inference)

| Stage | Medallion hypothesis | Public evidence |
|-------|---------------------|-----------------|
| Hypothesis | Scientist-led, long R&D | [[claim:CLM-2024-009]] |
| Data | Proprietary cleaning | [[claim:CLM-2026-019]] |
| Models | Ensemble / stat-arb | Phase III signals |
| Portfolio | Neutralized, vol-targeted | Phase V |
| Execution | Low drag | [[claim:CLM-2024-007]] |
| Risk | De-gross in stress | [[claim:CLM-2024-010]] contrast |

Peers may share stages; differentiation is **integration and secrecy**, not a single publicized invention.

Requirement: R6 (workflow deliverable)
