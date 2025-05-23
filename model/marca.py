class Marca:

    # metodo di inizializzazione
    def __init__(self, id=None, nome=None, autovetture=None):
        self.id = id
        self.nome = nome
        self.autovetture = autovetture if autovetture else []


    # metodo di deserializzazione (json -> Marca)
    @classmethod
    def deserializzazione(cls, json):
        return cls(**json)


    # metodo di serializzazione (Marca -> json)
    def serializzazione(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "autovetture": [autovettura.serializzazione_per_marca() for autovettura in self.autovetture]
        }


    # metodo di serializzazione per inclusione Marca nel json Autovettura
    def serializzazione_per_autovettura(self):
        return {
            "id": self.id,
            "nome": self.nome
        }
