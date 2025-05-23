from model.autovettura import Autovettura
from model.marca import Marca
from model.categoria import Categoria
from model.alimentazione import Alimentazione
from repository.repository import Repository


class AutovetturaService:

    # metodo di inizializzazione
    def __init__(self):
        self.repository = Repository()


    # metodo di servizio per endpoint elenco autovetture
    def elenco_autovetture(self):
        sql = "SELECT * FROM autovetture JOIN marche ON autovetture.id_marca=marche.id JOIN categorie ON autovetture.id_categoria=categorie.id JOIN alimentazioni ON autovetture.id_alimentazione=alimentazioni.id"
        ottenuto_db = self.repository.recupero_multiplo(sql)
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "mesaggio": ottenuto_db}, 500
        autovetture = []
        for record in ottenuto_db:
            marca = Marca(id=record[9], nome=record[10])
            categoria = Categoria(id=record[11], descrizione=record[12])
            alimentazione = Alimentazione(id=record[13], descrizione=record[14])   #record[numero]-> sono le posizione delle colonne nel database
            autovettura = Autovettura(id=record[0], modello=record[1], trasmissione=record[2], numero_porte=record[3],
                                      immagine=record[4], tariffa_giornaliera=record[5], marca=marca, categoria=categoria,
                                      alimentazione=alimentazione)
            autovetture.append(autovettura)
        return [autovettura.serializzazione() for autovettura in autovetture], 200


    # metodo di servizio per endpoint registrazione autovettura
    def registrazione_autovettura(self, corpo_richiesta):
        # validazione dati in entrata
        esito_validazione = Autovettura.validazione_registrazione(corpo_richiesta)
        if not esito_validazione[0]:
            return {"codice": 400, "mesaggio": esito_validazione[1]}, 400
        # deserializzazione completa json ricevuto
        autovettura = Autovettura.deserializzazione(corpo_richiesta)
        # controllo di esistenza oggetti "alto livello"
        if not isinstance(self.repository.recupero_singolo("SELECT id FROM marche WHERE id=%s", (autovettura.marca.id,)), tuple):
            return {"codice": 400, "messaggio": "Id Marca non valido o inesistente"}, 400
        if not isinstance(self.repository.recupero_singolo("SELECT id FROM categorie WHERE id=%s", (autovettura.categoria.id,)), tuple):
            return {"codice": 400, "messaggio": "Id Categoria non valido o inesistente"}, 400
        if not isinstance(self.repository.recupero_singolo("SELECT id FROM alimentazioni WHERE id=%s", (autovettura.alimentazione.id,)), tuple):
            return {"codice": 400, "messaggio": "Id Alimentazione non valido o inesistente"}, 400
        # registrazione autovettura
        sql = ("INSERT INTO autovetture (modello,trasmissione,numero_porte,immagine,tariffa_giornaliera,id_marca,id_categoria,id_alimentazione) "
               "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
        valori = (autovettura.modello, autovettura.trasmissione, autovettura.numero_porte, autovettura.immagine,
                  autovettura.tariffa_giornaliera, autovettura.marca.id, autovettura.categoria.id, autovettura.alimentazione.id)
        ottenuto_db = self.repository.manipolazione(sql, valori)
        if isinstance(ottenuto_db, str):
            return {"codice": 500, "messaggio": ottenuto_db}, 500
        return {"codice": 201, "messaggio": "Autovettura registrata"}, 201

