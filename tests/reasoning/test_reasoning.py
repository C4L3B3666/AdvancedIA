# tests/reasoning/test_reasoning.py

from src.reasoning.reasoning import ReasoningModule

def test_infer_returns_expected_output():
    module = ReasoningModule()
    input_data = "dados perceptivos"
    output = module.infer(input_data)
    assert output == f"Inferência sobre: {input_data}"
