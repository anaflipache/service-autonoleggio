from model.cliente import Cliente
from repository.repository import Repository
import base64
import time


class ClienteService:

    # metodo di inizializzazione (serve per creare l'oggetto di Repository necessario)
    def __init__(self):
        self.repository = Repository()


    # metodo di servizio per endpoint registrazione cliente
    def registrazione_cliente(self, corpo_richiesta):
        # validazione dati in entrata
        esito_validazione = Cliente.validazione_registrazione(corpo_richiesta)
        if not esito_validazione[0]:
            return {"codice": 400, "messaggio": esito_validazione[1]}, 400
        # convertiamo il json ricevuto in oggetto Cliente
        cliente = Cliente.deserializzazione(corpo_richiesta)
        print(cliente)
        # controllo univocità indirizzo mail
        if self.repository.recupero_singolo("SELECT id FROM clienti WHERE mail=%s", (cliente.mail,)):
            return {"codice": 409, "messaggio": "mail già presente"}, 409
        # inviamo l'oggetto Cliente al database
        sql = "INSERT INTO clienti (nome,cognome,mail,password,numero_patente, immagine_patente) VALUES (%s,%s,%s,%s,%s,%s)"
        valori = (cliente.nome, cliente.cognome, cliente.mail, cliente.password, cliente.numero_patente, cliente.immagine_patente)
        ottenuto_db = self.repository.manipolazione(sql, valori)
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        return {"codice": 201, "messaggio": "Cliente Registrato"}, 201


    # metodo di servizio per endpoint aggiornamento dati cliente
    def aggiornamento_cliente(self, corpo_richiesta, id):
        # validazione dati in entrata
        esito_validazione = Cliente.validazione_aggiornamento(corpo_richiesta)
        if not esito_validazione[0]:
            return {"codice": 400, "messaggio": esito_validazione[1]}, 400
        # controllo inesistenza id
        if self.dati_cliente(id)[1] != 200:
            return {"codice": 404, "messaggio": "Cliente non trovato"}, 404
        # convertiamo il json ricevuto in oggetto Cliente
        cliente = Cliente.deserializzazione(corpo_richiesta)
        # inviamo i nuovi dati del Cliente al database
        sql = "UPDATE clienti SET password=%s, numero_patente=%s, immagine_patente=%s WHERE id=%s"
        valori = cliente.password, cliente.numero_patente, cliente.immagine_patente, id
        ottenuto_db = self.repository.manipolazione(sql, valori)
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        return {"codice": 202, "messaggio": "Dati Cliente Aggiornati"}, 202


    # metodo di servizio per endpoint eliminazione cliente
    def eliminazione_cliente(self, id):
        ottenuto_db = self.repository.manipolazione("DELETE FROM clienti WHERE id=%s", (id,))
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        elif ottenuto_db == 0:
            return {"codice": 404, "messaggio": "Cliente non trovato"}, 404
        return {"codice": 202, "messaggio": "Cliente Eliminato"}, 202


    # metodo di servizio per endpoint dati cliente
    def dati_cliente(self, id):
        ottenuto_db = self.repository.recupero_singolo("SELECT * FROM clienti WHERE id=%s", (id))
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        elif not ottenuto_db:
            return {"codice": 404, "messaggio": "Cliente non trovato"}, 404
        return Cliente(*ottenuto_db).serializzazione(), 200


    # metodo di servizio per endpoint elenco clienti
    def elenco_clienti(self):
        ottenuto_db = self.repository.recupero_multiplo("SELECT * FROM clienti")
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        return [Cliente(*record).serializzazione() for record in ottenuto_db], 200


    # metodo di servizio per endpoint login cliente
    def login_cliente(self, corpo_richiesta):
        # verifica formattazione json in entrata
        if not corpo_richiesta.get("mail") or not corpo_richiesta.get("password"):
            return {"codice": 400, "messaggio": "Dati mancanti o errati"}, 400
        # conversione json in Cliente
        cliente = Cliente.deserializzazione(corpo_richiesta)
        # verifica login
        if not isinstance(self.repository.recupero_singolo("SELECT id FROM clienti WHERE mail=%s AND password=%s",
                                                           (cliente.mail, cliente.password)), tuple):
            return {"codice": 401, "messaggio": "Login non autorizzato"}, 401
        # generazione token (univoco per ogni cliente e per singolo login) e registrazione nel database
        auth_token = f"{base64.b64encode(cliente.mail.encode()).decode()}_{int(time.time())}"
        ottenuto_db = self.repository.manipolazione("UPDATE clienti SET auth_token=%s WHERE mail=%s",
                                                    (auth_token, cliente.mail))
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        return {"codice": 200, "token": auth_token}, 200


    # metodo di servizio per endpoint logout cliente
    def logout_cliente(self, auth_token):
        # verifica validità token
        if not isinstance(self.repository.recupero_singolo("SELECT id FROM clienti WHERE auth_token=%s",
                                                           (auth_token,)), tuple):
            return {"codice": 401, "messaggio": "Operazione non autorizzata"}, 401
        # annullamento token
        ottenuto_db = self.repository.manipolazione("UPDATE clienti SET auth_token=null WHERE auth_token=%s",
                                                    (auth_token,))
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        return {"codice": 200, "messaggio": "Logout avvenuto"}, 200


