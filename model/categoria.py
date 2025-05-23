class Categoria:

    # metodo di inizializzazione
    def __init__(self, id=None, descrizione=None, autovetture=None):
        self.id = id
        self.descrizione = descrizione
        self.autovetture = autovetture if autovetture else []


    # metodo di deserializzazione (json -> Categoria)
    @classmethod
    def deserializzazione(cls, json):
        return cls(**json)


    # metodo di serializzazione (Categoria -> json)
    def serializzazione(self):
        return self.__dict__


    # metodo di serializzazione per inclusione Categoria nel json Autovettura
    def serializzazione_per_autovettura(self):
        return {
            "id": self.id,
            "descrizione": self.descrizione
        }