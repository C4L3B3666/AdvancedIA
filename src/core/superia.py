# src/core/superia.py

from src.perception.perception import PerceptionModule
from src.reasoning.reasoning import ReasoningModule
from src.decision.decision import DecisionModule

class SuperIA:
    def __init__(self):
        self.perception = PerceptionModule()
        self.reasoning = ReasoningModule()
        self.decision = DecisionModule()

    def run(self, input_data):
        perception_result = self.perception.process(input_data)
        reasoning_result = self.reasoning.infer(perception_result)
        decision_result = self.decision.decide(reasoning_result)
        return decision_result
