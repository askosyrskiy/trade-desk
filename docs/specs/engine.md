# Engine

A `Session` is: one `Strategy` + one `Broker` + one `RiskPolicy` + one `SessionMode`.

The engine may:

- pull quotes through the broker port and push them into the strategy
- collect `Intent`s from the strategy
- in `confirm` mode, send an order only after `Session.confirm`
- in `auto` mode, send without a click (not used for SPX iron fly yet)
- flatten on disconnect if the risk policy says so

The engine must not import `trade_desk.brokers.tradier` or `trade_desk.strategies.spx_iron_fly`. Wiring happens in the app composition root (`trade_desk.web.app` today).
