# EXP-09 finish checklist

Check items in order. Do not mark a block done until every box in it is checked.

## 1. Simulation

File: [src/medallion/simulation.py](../../src/medallion/simulation.py). Function: `simulate_baum_welch_lineage`. NumPy only. Do not add `hmmlearn`.

- [ ] Two-state Gaussian HMM
- [ ] Log-space forward–backward
- [ ] Baum–Welch EM
- [ ] Label alignment by matching learned means to true means (state IDs do not flip)
- [ ] Era 1: sticky transitions, separated emissions (low-vol drift vs high-vol). Seed `19`. `n_days` `1260`
- [ ] Fit Baum–Welch on era 1 only
- [ ] Trade the one-step predictive mean from the filtered probability at t−1
- [ ] Costs via existing `CostModel` on position changes
- [ ] Era 2: true chain becomes fast-switching and drift signs weaken (1989-style break)
- [ ] Era 2 policy: frozen era-1 parameters
- [ ] Era 2 policy: Baum–Welch refit on era 2
- [ ] Era 2 policy: short-horizon mean reversion, position = −rolling z-score, no latent state
- [ ] Oracle-state Sharpe on era 1 only, labeled non-tradable

## 2. Experiment package

Directory: [experiments/09_baum_welch/](../../experiments/09_baum_welch/).

- [ ] `contract.yaml` with hypothesis: in-regime filtered net Sharpe is positive and state recovery is high; after the break, frozen HMM net Sharpe falls; the short-horizon sleeve does not require the latent state to stay valid
- [ ] Contract limitations: synthetic; not Ax’s parameterization; not a Medallion return; speech-HMM lineage excluded; EXP-08 remains the non-HMM gate
- [ ] Contract links SIG-005
- [ ] `run.py` writes `results/summary.json`
- [ ] `README.md` states how to run it and what it does not prove
- [ ] Frozen `results/summary.json` includes `gross_sharpe` and `net_sharpe` (era-1 filtered HMM)
- [ ] Summary includes `era1_state_accuracy`
- [ ] Summary includes `era2_frozen_net_sharpe`, `era2_refit_net_sharpe`, `era2_short_horizon_net_sharpe`
- [ ] Summary includes `oracle_net_sharpe` (era 1 only)
- [ ] Summary includes `sensitivity.sweeps` over `commission_bps` on the era-1 net Sharpe

## 3. QA wiring

- [ ] [Makefile](../../Makefile) `smoke` runs `experiments/09_baum_welch/run.py`
- [ ] [scripts/validate_experiment_summaries.py](../../scripts/validate_experiment_summaries.py) lists `09_baum_welch` in `SMOKE_DIRS`
- [ ] [tests/test_simulation.py](../../tests/test_simulation.py): era-1 state accuracy above 0.7 on seed 19
- [ ] Same test: era-1 net Sharpe is at most gross Sharpe

## 4. Corpus links

- [ ] [data/signals.yaml](../../data/signals.yaml) SIG-005 points at EXP-09
- [ ] SIG-005 `era_plausibility` is late 1970s–present
- [ ] SIG-005 stays evidence level E1 and replication `partial`
- [ ] SIG-005 paragraph in [research/phase_03_signals/core_stat_arb.md](../../research/phase_03_signals/core_stat_arb.md) points at EXP-09
- [ ] [quarto/chapters/07-experiments.qmd](../../quarto/chapters/07-experiments.qmd) includes the frozen JSON
- [ ] Row in [research/phase_07_compute/README.md](../../research/phase_07_compute/README.md): frozen slow HMM fails a fast-switch break; does not prove RenTech used a two-state HMM
- [ ] Same row in [research/phase_08_synthesis/experiment_integration.md](../../research/phase_08_synthesis/experiment_integration.md)
- [ ] [docs/traceability.md](../../docs/traceability.md) R7 path is `experiments/03–09`
- [ ] [CHANGELOG.md](../../CHANGELOG.md) Unreleased note. No version bump. No git tag.

## 5. Verify

- [ ] `make test` passes
- [ ] `make smoke` passes
- [ ] `make quarto-check` passes if Quarto is on `PATH`
