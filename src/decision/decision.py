# src/decision/decision.py

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

class DecisionModule:
    def __init__(self):
        logger.info("DecisionModule inicializado.")

    def decide(self, inference):
        logger.info(f"Tomando decisão com base na inferência: {inference}")
        if "alerta" in inference.lower():
            decision = "Emitir alerta"
        else:
            decision = "Continuar operação"
        logger.info(f"Decisão tomada: {decision}")
        return decision
