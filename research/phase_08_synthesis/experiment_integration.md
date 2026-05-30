# Experiment integration (toys) {#experiment-integration}

**Last updated:** 2026-05-28

Frozen JSON in [Chapter VII](../chapters/07-experiments.html) comes from `make smoke`. **None** replicate Medallion returns.

| ID | Proves (directional) | Does not prove |
|----|----------------------|----------------|
| EXP-03 | Costs erode mean-reversion net Sharpe | Real equity microstructure alpha |
| EXP-04 | Impact + fees can overwhelm execution edge | RenTech execution is the main alpha source |
| EXP-05 | Vol targeting interacts with costs | Reported Sharpe levels |
| EXP-06 | VRP carry faces cost drag | Listed options PnL at Medallion |
| EXP-07 | Ensemble can differ from single sleeves | Optimal signal weights |
| EXP-08 | Regime gating changes blended toy Sharpe | HMM fit at RenTech |

Sensitivity grids (EXP-03/04/05) support **monotonic cost drag** and **participation impact** claims in the test plan.
