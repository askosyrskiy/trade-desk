# Captain's Log

Semi-manual UI for SPX 0DTE iron fly, modeled on Dale's Excel sheet (shared 20 Aug 2026).

Route: `/iron-fly`

## Spot strip

| Sheet            | Field        |
|------------------|--------------|
| Last Price       | `last_price` |
| Watch + Add      | `watch_spot`, `watch_add`, `watch_var` |
| Next Move + Add  | `next_spot`, `next_add`, `next_var` |
| Strike / Var     | `atm_strike` |
| Wings            | `wings` put/call |

## Opportunity

Max Opp $, Remaining Opp $, used close %, BTC remaining %. Session-level, not per fly.

## Blotter F1–F40

Fly, Strike, Status (empty / active / closed), Put, Call, STO, BTC actual, BTC est, Net, Max.

Actions: Add watch, Add next, Flatten — disabled until `Session.confirm` routes to a broker.

The first render uses **sample** rows so the page exists before Tradier quotes.
