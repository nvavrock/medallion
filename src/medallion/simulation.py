"""Cost- and capacity-aware toy simulations for hypothesis testing."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass
class CostModel:
    commission_bps: float = 1.0
    slippage_bps: float = 2.0

    def round_trip_cost(self) -> float:
        return (self.commission_bps + self.slippage_bps) * 2 / 10_000


@dataclass
class BacktestResult:
    gross_sharpe: float
    net_sharpe: float
    max_drawdown: float
    turnover: float
    capacity_breach_pct: float


def simulate_mean_reversion(
    n_days: int = 252 * 5,
    signal_strength: float = 0.02,
    noise: float = 0.01,
    cost: CostModel | None = None,
    max_gross_exposure: float = 1.0,
    capacity_aum_musd: float = 500.0,
    trade_size_musd: float = 1.0,
    seed: int = 42,
) -> BacktestResult:
    """
    Toy mean-reversion: position = -zscore(returns), with costs on position changes.
    capacity_breach_pct: fraction of days where |position| * trade_size exceeds soft capacity.
    """
    rng = np.random.default_rng(seed)
    cost = cost or CostModel()
    returns = rng.normal(0, noise, n_days)
    prices = np.exp(np.cumsum(returns))
    series = pd.Series(prices)
    z = (series - series.rolling(20).mean()) / series.rolling(20).std()
    position = (-z / z.abs().rolling(60).max()).clip(-1, 1).fillna(0) * max_gross_exposure
    strat_returns = position.shift(1).fillna(0) * pd.Series(returns)
    turnover = position.diff().abs().fillna(0)
    cost_drag = turnover * cost.round_trip_cost()
    net = strat_returns - cost_drag

    cap_breach = (turnover * trade_size_musd > capacity_aum_musd * 0.01).mean()

    def sharpe(x: pd.Series) -> float:
        if x.std() == 0:
            return 0.0
        return float(x.mean() / x.std() * np.sqrt(252))

    gross_dd = float((strat_returns.cumsum() - strat_returns.cumsum().cummax()).min())
    net_dd = float((net.cumsum() - net.cumsum().cummax()).min())

    return BacktestResult(
        gross_sharpe=sharpe(strat_returns),
        net_sharpe=sharpe(net),
        max_drawdown=min(gross_dd, net_dd),
        turnover=float(turnover.mean()),
        capacity_breach_pct=float(cap_breach),
    )


def almgren_chriss_impact(
    participation_rate: float,
    volatility: float,
    eta: float = 0.142,
    gamma: float = 0.314,
) -> float:
    """
    Simplified AC temporary + permanent impact (dimensionless scale).
    participation_rate: fraction of ADV traded per day.
    """
    temp = eta * volatility * participation_rate
    perm = gamma * volatility * participation_rate
    return temp + perm


def simulate_execution_edge(
    n_trades: int = 10_000,
    edge_bps: float = 0.5,
    cost: CostModel | None = None,
    participation_rate: float = 0.01,
    volatility: float = 0.02,
    seed: int = 0,
) -> dict[str, float]:
    """Can execution edge alone explain high Sharpe? Toy aggregation."""
    rng = np.random.default_rng(seed)
    cost = cost or CostModel()
    impact = almgren_chriss_impact(participation_rate, volatility)
    per_trade_net = edge_bps / 10_000 - cost.round_trip_cost() - impact
    draws = rng.normal(per_trade_net, 0.0002, n_trades)
    daily = pd.Series(draws).groupby(np.arange(n_trades) // 40).sum()
    sharpe = float(daily.mean() / daily.std() * np.sqrt(252)) if daily.std() > 0 else 0.0
    return {
        "mean_net_per_trade": float(draws.mean()),
        "sharpe_aggregated": sharpe,
        "impact_per_trade": impact,
    }


def vol_target_kelly_simulation(
    n_days: int = 252 * 10,
    true_sharpe: float = 1.5,
    target_vol: float = 0.15,
    leverage_band: tuple[float, float] = (5.0, 12.0),
    cost: CostModel | None = None,
    seed: int = 1,
) -> dict[str, float]:
    """Vol-target sizing with leverage clipped to band; reports gross vs net Sharpe."""
    rng = np.random.default_rng(seed)
    cost = cost or CostModel()
    daily_ret = rng.normal(true_sharpe / np.sqrt(252), 1 / np.sqrt(252), n_days)
    realized_vol = pd.Series(daily_ret).rolling(20).std() * np.sqrt(252)
    lev = (target_vol / realized_vol).clip(leverage_band[0], leverage_band[1]).fillna(leverage_band[0])
    gross = lev.shift(1).fillna(1) * daily_ret
    turnover = lev.diff().abs().fillna(0)
    net = gross - turnover * cost.round_trip_cost()

    def sharpe(x: pd.Series) -> float:
        return float(x.mean() / x.std() * np.sqrt(252)) if x.std() > 0 else 0.0

    return {
        "gross_sharpe": sharpe(pd.Series(gross)),
        "net_sharpe": sharpe(pd.Series(net)),
        "mean_leverage": float(lev.mean()),
    }
