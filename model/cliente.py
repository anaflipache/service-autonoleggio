from cerberus import Validator

class Cliente:

    # attributo di classe per schema di validazione dati di registrazione
    schema_registrazione = {
        "nome": {
            "required": True,
            "type": "string",
            "regex": "^[a-zA-Zàèìòù\\s']{1,50}$"
        },
        "cognome": {
            "required": True,
            "type": "string",
            "regex": "^[a-zA-Zàèìòù\\s']{1,50}$"
        },
        "mail": {
            "required": True,
            "type": "string",
            "regex": "^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\\.[a-zA-Z]{2,6}$"
        },
        "password": {
            "required": True,
            "type": "string",
            "regex": "^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{6,10}$"
        },
        "numero_patente": {
            "required": True,
            "type": "string",
            "regex": "^[A-Z\\d]{1,20}$"
        }
    }


    # attributo di classe per schema di validazione dati di aggiornamento
    schema_aggiornamento = {
        "password": {
            "required": True,
            "type": "string",
            "regex": "^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{6,10}$"
        },
        "numero_patente": {
            "required": True,
            "type": "string",
            "regex": "^[A-Z\\d]{1,20}$"
        },
        "immagine_patente": {
            "required": True,
            "type": "string",
            "nullable": True
        }

    }


    # metodo di inizializzazione 
    def __init__(self, id=None, nome=None, cognome=None, mail=None, password=None, numero_patente=None, immagine_patente=None, auth_token=None):
        self.id = id
        self.nome = nome
        self.cognome = cognome
        self.mail = mail
        self.password = password
        self.numero_patente = numero_patente
        self.immagine_patente = immagine_patente
        self.auth_token = auth_token


    # metodo di deserializzazione (json -> Cliente)
    @classmethod
    def deserializzazione(cls, json):
        return cls(**json)


    # metodo di serializzazione (Cliente -> json)
    def serializzazione(self):
        return self.__dict__


    # metodo per validazione dati di registrazione
    @classmethod
    def validazione_registrazione(cls, json):
        validatore = Validator(cls.schema_registrazione)
        if validatore.validate(json):
            return True,
        else:
            return False, validatore.errors


    # metodo per validazione dati di aggiornamento
    @classmethod
    def validazione_aggiornamento(cls, json):
        validatore = Validator(cls.schema_aggiornamento)
        if validatore.validate(json):
            return True,
        else:
            return False, validatore.errors
