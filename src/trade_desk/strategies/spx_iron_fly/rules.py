"""Dale-style 0DTE iron fly scale rules. Pure functions — no I/O."""

from __future__ import annotations

from dataclasses import dataclass


CREDIT_CUTOFF = 15.0
TIGHT_MOVE = 7.0
TIGHT_OFFSET = 10.0
WIDE_MOVE = 10.0
WIDE_OFFSET = 15.0


@dataclass(frozen=True)
class ScaleMode:
    """How later flies are spaced after the first fill credit is known."""

    name: str
    move_points: float
    offset_points: float
    from_first_short: bool


def scale_mode(first_credit: float) -> ScaleMode:
    """Credit <= 15 → add on a 7-pt move, 10 pts from the *first* short.
    Credit > 15 → add on a 10-pt move, 15 pts from the *previous* short.
    """
    if first_credit <= CREDIT_CUTOFF:
        return ScaleMode("tight", TIGHT_MOVE, TIGHT_OFFSET, from_first_short=True)
    return ScaleMode("wide", WIDE_MOVE, WIDE_OFFSET, from_first_short=False)


def add_short_strike(
    *,
    first_short: float,
    previous_short: float,
    direction: int,
    mode: ScaleMode,
) -> float:
    """direction is +1 (up) or -1 (down)."""
    if direction not in (-1, 1):
        raise ValueError("direction must be +1 or -1")
    anchor = first_short if mode.from_first_short else previous_short
    return anchor + direction * mode.offset_points


def max_loss_per_share(wing_width: float, credit: float) -> float:
    return wing_width - credit


def breakevens(short_strike: float, credit: float) -> tuple[float, float]:
    return short_strike - credit, short_strike + credit
