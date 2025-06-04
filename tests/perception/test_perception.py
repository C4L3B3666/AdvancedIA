# src/perception/perception.py

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

class PerceptionModule:
    def __init__(self):
        logger.info("PerceptionModule inicializado.")

    def process(self, data):
        logger.info(f"Processando dados de entrada: {data}")
        result = data  # Em versões futuras, haverá pré-processamento aqui
        logger.info(f"Resultado do processamento: {result}")
        return result
