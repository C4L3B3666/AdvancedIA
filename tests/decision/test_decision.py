# tests/decision/test_decision.py

from src.decision.decision import DecisionModule

def test_decide_returns_alert():
    module = DecisionModule()
    inference = "Alerta detectado no sistema"
    decision = module.decide(inference)
    assert decision == "Emitir alerta"

def test_decide_returns_continue():
    module = DecisionModule()
    inference = "Tudo normal"
    decision = module.decide(inference)
    assert decision == "Continuar operação"
