# SPX 0DTE iron fly

Interview rules (Dale Perryman / Theta Profits), frozen here as the spec for `spx_iron_fly`.

## Structure

Sell ATM call + ATM put, buy wings (typically 40–50 wide), same-day SPX expiration. Cash-settled.

## Session

- First fly ~10:30–11:00 ET, ATM or nearest listed strike.
- If first **fill** credit ≤ $15: next add when spot moves 7 pts; new short 10 pts from the **first** short.
- If first fill credit > $15: next add when spot moves 10 pts; new short 15 pts from the **previous** short.
- Close a fly near 90–100% of max loss (practically: spot tags breakeven).
- Let winners run (last-hour theta).
- Stand down on major news (CPI, FOMC, NFP).

## Mode

`confirm`. The Captain's Log computes Watch / Next Move; Add and Close wait for a click.

## Open questions (do not guess in code)

- SPX vs SPXW root on Tradier
- Max concurrent flies
- Whether adds fire both directions independently
- Limit offset vs mid for the credit
- Young-fly “drop fast” vs keep round 00 strikes (from the 20 Aug 2026 session chat)

Record answers in `docs/decisions/` before encoding them.
