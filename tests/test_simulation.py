from medallion.simulation import (
    CostModel,
    simulate_execution_edge,
    simulate_mean_reversion,
    vol_target_kelly_simulation,
)


def test_mean_reversion_net_below_gross():
    cost = CostModel(commission_bps=2, slippage_bps=3)
    r = simulate_mean_reversion(cost=cost, seed=1)
    assert r.net_sharpe <= r.gross_sharpe + 0.01


def test_execution_edge_returns_metrics():
    m = simulate_execution_edge(seed=2)
    assert "sharpe_aggregated" in m


def test_vol_target_leverage_band():
    m = vol_target_kelly_simulation(seed=3)
    assert m["mean_leverage"] >= 5.0
    assert m["net_sharpe"] <= m["gross_sharpe"] + 0.01
