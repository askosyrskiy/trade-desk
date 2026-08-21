"""Captain's Log view model. Fixture-backed until the engine is live."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Literal


@dataclass
class FlyRow:
    slot: int
    strike: float | None
    status: Literal["empty", "active", "closed"]
    put_wing: int | None = None
    call_wing: int | None = None
    sto: float | None = None
    btc_actual: float | None = None
    btc_est: float | None = None
    net: float | None = None
    max_loss: float | None = None


@dataclass
class CaptainsLog:
    last_price: float
    watch_spot: float
    watch_add: float
    watch_var: float
    next_spot: float
    next_add: float
    next_var: float
    atm_strike: float
    wings: int
    max_opp: float
    remaining_opp: float
    used_close_pct: float
    btc_remaining_pct: float
    auto_refresh: bool
    flies: list[FlyRow]

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


def empty_blotter(slots: int = 40) -> list[FlyRow]:
    return [FlyRow(slot=i, strike=None, status="empty") for i in range(1, slots + 1)]


def sample_log() -> CaptainsLog:
    """Layout sample so /iron-fly renders before quotes are wired.
    Numbers echo the 20 Aug 2026 Captain's Log share, labeled as sample.
    """
    flies = empty_blotter()
    samples = [
        FlyRow(1, 7890, "closed", 50, 50, 30.45, 21.55, 13.20, -1.10, 29),
        FlyRow(2, 7870, "active", 50, 50, 30.05, 16.20, 6.65, -1.35, 27),
        FlyRow(3, 7890, "closed", 50, 50, 13.00, None, 16.20, -1.20, 27),
        FlyRow(4, 7925, "closed", 50, 50, 13.40, 17.00, None, -1.65, 27),
        FlyRow(5, 7875, "active", 50, 50, 14.13, None, 13.55, 1.20, 35),
        FlyRow(6, 7885, "active", 50, 50, 14.75, None, None, None, None),
    ]
    for row in samples:
        flies[row.slot - 1] = row
    return CaptainsLog(
        last_price=7666.48,
        watch_spot=7677.5,
        watch_add=7680,
        watch_var=11.02,
        next_spot=7662.5,
        next_add=7660,
        next_var=-3.98,
        atm_strike=7685,
        wings=50,
        max_opp=3785,
        remaining_opp=2738,
        used_close_pct=27.6,
        btc_remaining_pct=73,
        auto_refresh=True,
        flies=flies,
    )
