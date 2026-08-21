from trade_desk.strategies.spx_iron_fly.rules import add_short_strike, breakevens, scale_mode


def test_tight_mode_when_credit_at_cutoff():
    mode = scale_mode(15)
    assert mode.name == "tight"
    assert mode.move_points == 7
    assert mode.offset_points == 10
    assert add_short_strike(
        first_short=6040, previous_short=6040, direction=1, mode=mode
    ) == 6050


def test_wide_mode_offsets_from_previous():
    mode = scale_mode(18)
    assert mode.name == "wide"
    assert add_short_strike(
        first_short=6040, previous_short=6055, direction=1, mode=mode
    ) == 6070


def test_breakevens_use_credit_not_wing():
    lo, hi = breakevens(6040, 29.65)
    assert lo == 6010.35
    assert hi == 6069.65
