from trade_desk.brokers.tradier import TradierBroker
from trade_desk.engine import Session
from trade_desk.strategies.spx_iron_fly import SpxIronFly


def test_session_composes_ports_without_calling_the_broker():
    session = Session(strategy=SpxIronFly(), broker=TradierBroker())
    model = session.view_model()
    assert model["strategy"] == "spx-iron-fly"
    assert model["broker"] == "tradier"
    assert model["mode"] == "confirm"
    assert len(model["flies"]) == 40
