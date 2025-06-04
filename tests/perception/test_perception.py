# tests/perception/test_perception.py

from src.perception.perception import PerceptionModule

def test_process_returns_input():
    module = PerceptionModule()
    input_data = "teste"
    output = module.process(input_data)
    assert output == input_data
