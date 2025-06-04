# tests/core/test_superia.py

from src.core.superia import SuperIA

def test_superia_alert_decision():
    ia = SuperIA()
    input_data = "Existe um alerta de segurança"
    result = ia.run(input_data)
    assert result == "Emitir alerta"

def test_superia_normal_decision():
    ia = SuperIA()
    input_data = "Todos os sistemas operando normalmente"
    result = ia.run(input_data)
    assert result == "Continuar operação"
