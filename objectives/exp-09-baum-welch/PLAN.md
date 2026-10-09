# EXP-09 — Baum–Welch lineage toy

Repo copy of the Cursor plan so it can be opened from GitHub. Local original: `/home/me/.cursor/plans/baum-welch_experiment_3abbf145.plan.md`.

Add a seeded Baum–Welch experiment that shows what the repo’s “Baum/Ax lineage” claim actually is: a slow two-state model that works in-regime and fails after a 1989-style break, while a short-horizon sleeve does not depend on that latent state.

## Todos

- [ ] Add `simulate_baum_welch_lineage` (2-state EM, era break, three policies, costs) in `src/medallion/simulation.py`
- [ ] Add `experiments/09_baum_welch` contract, `run.py`, README, and frozen `summary.json`
- [ ] Wire Makefile smoke, summary validator, and a unit test for state recovery and net vs gross
- [ ] Link SIG-005, Chapter III/VII, experiment integration, traceability, and CHANGELOG to EXP-09

## What the lineage is

The corpus already states the dates and then stops. [research/phase_01_history/timeline.md](../../research/phase_01_history/timeline.md) says Medallion (1988) “builds on Baum/Ax model lineage” ([[claim:CLM-2026-004]]). The public build, from claims already in the repo, is:

- **Baum:** statistical currency models; Baum–Welch is his HMM algorithm. He later left pure systematic modeling ([[claim:CLM-2026-010]]).
- **Ax:** kept the systematic book and widened it from currencies to commodity futures; that book is the Medallion predecessor. He left after the 1989 drawdown ([[claim:CLM-2026-011]], [[claim:CLM-2026-005]]).
- **The build on that lineage** is not a bigger HMM. Berlekamp, Straus, and Laufer replaced a concentrated model book with short-horizon statistical bets ([[claim:CLM-2026-006]]).
- **Mercer/Brown** are a later IBM-speech HMM culture ([[claim:CLM-2024-006]]), not a continuation of Ax’s futures models. Leave them out of this toy.

[experiments/08_regime_filter](../../experiments/08_regime_filter) is a rolling-vol gate. Its contract says “Not HMM estimation.” [SIG-005](../../data/signals.yaml) is still E1 and dated “1990s–present,” which skips the 1978–1989 book this experiment is about.

No public source gives state count, emissions, or holding period. The executable will not invent those as RenTech facts.

## Experiment

New directory [experiments/09_baum_welch/](../../experiments/09_baum_welch/) with `contract.yaml`, `run.py`, `README.md`, and frozen `results/summary.json`.

Implement `simulate_baum_welch_lineage` in [src/medallion/simulation.py](../../src/medallion/simulation.py). NumPy only (no `hmmlearn`). Two-state Gaussian HMM, log-space forward–backward, Baum–Welch EM, label alignment by matching learned means to true means so state IDs do not flip.

Seeded DGP (`n_days` per era 1260, `seed` 19):

- **Era 1 (Baum/Ax analogue):** sticky transitions, separated emissions (low-vol drift vs high-vol). Fit Baum–Welch on era 1 only. Trade the one-step predictive mean from the filtered probability at t−1. Apply the existing [CostModel](../../src/medallion/simulation.py) on position changes.
- **Era 2 (1989-style break):** the true chain becomes fast-switching and the drift signs weaken, so a frozen slow HMM’s state bets go stale. Score three policies on era 2 with the same costs:
  - frozen era-1 parameters
  - Baum–Welch refit on era 2
  - short-horizon mean reversion (position = −rolling z-score), no latent state — the Berlekamp-style analogue

Hypothesis written into the contract: in-regime filtered net Sharpe is positive and state recovery is high; after the break, the frozen HMM net Sharpe falls, and the short-horizon sleeve is the one that does not require the latent state to stay valid. Oracle-state Sharpe is reported as a non-tradable ceiling.

`summary.json` fields:

- `gross_sharpe` / `net_sharpe` — era-1 filtered HMM (so [scripts/validate_experiment_summaries.py](../../scripts/validate_experiment_summaries.py) still checks net ≤ gross)
- `era1_state_accuracy`
- `era2_frozen_net_sharpe`, `era2_refit_net_sharpe`, `era2_short_horizon_net_sharpe`
- `oracle_net_sharpe` (era 1 only)
- `sensitivity.sweeps` over `commission_bps` on the era-1 net Sharpe

Limitations in the contract: synthetic; not Ax’s parameterization; not a Medallion return; speech-HMM lineage excluded; EXP-08 remains the non-HMM gate.

## Wiring

- [Makefile](../../Makefile) `smoke` target: run `experiments/09_baum_welch/run.py`
- [scripts/validate_experiment_summaries.py](../../scripts/validate_experiment_summaries.py): add `09_baum_welch` to `SMOKE_DIRS`
- [tests/test_simulation.py](../../tests/test_simulation.py): era-1 state accuracy above 0.7 on seed 19, and era-1 net Sharpe ≤ gross
- [quarto/chapters/07-experiments.qmd](../../quarto/chapters/07-experiments.qmd): include the frozen JSON
- Point SIG-005 and the SIG-005 paragraph in [research/phase_03_signals/core_stat_arb.md](../../research/phase_03_signals/core_stat_arb.md) at EXP-09; set `era_plausibility` to late 1970s–present. Keep evidence level E1. Replication stays `partial`.
- One row each in [research/phase_07_compute/README.md](../../research/phase_07_compute/README.md) and [research/phase_08_synthesis/experiment_integration.md](../../research/phase_08_synthesis/experiment_integration.md): proves a frozen slow HMM fails a fast-switch break; does not prove RenTech used a two-state HMM.
- [docs/traceability.md](../../docs/traceability.md): R7 path `experiments/03–09`
- [CHANGELOG.md](../../CHANGELOG.md): Unreleased note. No version bump and no tag.

Run `make test` and `make smoke` after the code exists. `make quarto-check` if Quarto is on PATH.
