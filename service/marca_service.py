from model.marca import Marca
from model.autovettura import Autovettura
from model.categoria import Categoria
from model.alimentazione import Alimentazione
from repository.repository import Repository


class MarcaService:

    # metodo di inizializzazione
    def __init__(self):
        self.repository = Repository()


    # metodo di servizio per endpoint elenco marche
    def elenco_marche(self):
        # ottenimento di tutte le marche
        sql_marche = "SELECT * FROM marche"
        ottenuto_db_marche = self.repository.recupero_multiplo(sql_marche)
        if isinstance(ottenuto_db_marche, str):
            return {"codice": 500, "messaggio": ottenuto_db_marche}, 500
        # ottenimento di tutte le auto (query unica e meno round-trip sul db)
        sql_autovetture = "SELECT * FROM autovetture JOIN categorie ON autovetture.id_categoria=categorie.id JOIN alimentazioni ON autovetture.id_alimentazione=alimentazioni.id"
        ottenuto_db_auto = self.repository.recupero_multiplo(sql_autovetture)
        if isinstance(ottenuto_db_auto, str):
            return {"codice": 500, "messaggio": ottenuto_db_auto}, 500
        # popolamento lista Marche con relative Autovetture
        marche = []
        for record_marca in ottenuto_db_marche:
            marca = Marca(id=record_marca[0], nome=record_marca[1])
            for record_auto in ottenuto_db_auto:
                if marca.id == record_auto[6]:
                    categoria = Categoria(id=record_auto[9], descrizione=record_auto[10])
                    alimentazione = Alimentazione(id=record_auto[11], descrizione=record_auto[12])
                    autovettura = Autovettura(id=record_auto[0], modello=record_auto[1],
                                              trasmissione=record_auto[2], numero_porte=record_auto[3],
                                              immagine=record_auto[4], tariffa_giornaliera=record_auto[5],
                                              categoria=categoria, alimentazione=alimentazione)
                    marca.autovetture.append(autovettura)
            marche.append(marca)
        return [marca.serializzazione() for marca in marche], 200
