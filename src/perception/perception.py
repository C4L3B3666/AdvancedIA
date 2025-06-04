class PerceptionModule:
    """
        #Saída 1

    """

    def __init__(self, config: dict = None):
        """
        Construtor do módulo de percepção.
            #Saida 2
        """
        self.config = config or {}

    def process(self, data):
        """
            #Mais tarde!
        """
        return data

if __name__ == "__main__":
    pm = PerceptionModule(config={"dummy": True})
    sample_input = [1, 2, 3]
    output = pm.process(sample_input)
    print("Saída de teste:", output)