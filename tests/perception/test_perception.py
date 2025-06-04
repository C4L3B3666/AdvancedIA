# tests/perception/test_perception.py

from src.perception.perception import PerceptionModule
# from perception.perception import PerceptionModule

def test_process_returns_same_data():
    """
    """
    pm = PerceptionModule()
    input_data = [1, 2, 3]
    output = pm.process(input_data)

    assert output == input_data, "Saída não CORRESPONDENTE!"