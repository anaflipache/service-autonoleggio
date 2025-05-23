from cerberus import Validator
from model.alimentazione import Alimentazione
from model.categoria import Categoria
from model.marca import Marca


class Autovettura:

    # attributo di classe per schema di validazione dati in entrata (registrazione)
    schema_registrazione = {
        "modello": {
            "required": True,
            "type": "string",
            "regex": "^[A-Z0-9\\s!-]{1,50}$"
        },
        "trasmissione": {
            "required": True,
            "type": "string",
            "regex": "^[MA]{1}$"
        },
        "numero_porte": {
            "required": True,
            "type": "integer"
        },
        "immagine": {
            "required": True,
            "type": "string",
            "nullable": True
        },
        "tariffa_giornaliera": {
            "required": True,
            "type": "float"
        },
        "marca": {
            "required": True,
            "type": "dict",
            "schema": {
                "id": {
                    "required": True,
                    "type": "integer",
                    "min": 1
                }
            }
        },
        "categoria": {
            "required": True,
            "type": "dict",
            "schema": {
                "id": {
                    "required": True,
                    "type": "integer",
                    "min": 1
                }
            }
        },
        "alimentazione": {
            "required": True,
            "type": "dict",
            "schema": {
                "id": {
                    "required": True,
                    "type": "integer",
                    "min": 1
                }
            }
        }
    }



    # metodo di inizializzazione
    def __init__(self, id=None, modello=None, trasmissione=None, numero_porte=None, immagine=None, tariffa_giornaliera=None,
                 marca=None, categoria=None, alimentazione=None):
        self.id = id
        self.modello = modello
        self.trasmissione = trasmissione
        self.numero_porte = numero_porte
        self.immagine = immagine
        self.tariffa_giornaliera = tariffa_giornaliera
        self.marca = marca
        self.categoria = categoria
        self.alimentazione = alimentazione


    # metodo di deserializzazione (json -> Autovettura)
    @classmethod
    def deserializzazione(cls, json):
        return cls(
            modello=json.get("modello"),
            trasmissione=json.get("trasmissione"),
            numero_porte=json.get("numero_porte"),
            immagine=json.get("immagine"),
            tariffa_giornaliera=json.get("tariffa_giornaliera"),
            marca=Marca.deserializzazione(json.get("marca")),
            categoria=Categoria.deserializzazione(json.get("categoria")),
            alimentazione=Alimentazione.deserializzazione(json.get("alimentazione"))
        )


    # metodo di serializzazione (Autovettura -> json)
    def serializzazione(self):
        return {
            "id": self.id,
            "modello": self.modello,
            "trasmissione": self.trasmissione,
            "numero_porte": self.numero_porte,
            "immagine": self.immagine,
            "tariffa_giornaliera": self.tariffa_giornaliera,
            "marca": self.marca.serializzazione_per_autovettura(),
            "categoria": self.categoria.serializzazione_per_autovettura(),
            "alimentazione": self.alimentazione.serializzazione_per_autovettura()
        }


    # metodo di serializzazione per inclusione Autovettura in json Marca
    def serializzazione_per_marca(self):
        return {
            "id": self.id,
            "modello": self.modello,
            "trasmissione": self.trasmissione,
            "numero_porte": self.numero_porte,
            "immagine": self.immagine,
            "tariffa_giornaliera": self.tariffa_giornaliera,
            "categoria": self.categoria.serializzazione_per_autovettura(),
            "alimentazione": self.alimentazione.serializzazione_per_autovettura()
        }


    # metodo per validazione dati in entrata (registrazione)
    @classmethod
    def validazione_registrazione(cls, json):
        validatore = Validator(cls.schema_registrazione)
        if validatore.validate(json):
            return True,
        else:
            return False, validatore.errors
