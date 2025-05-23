from flask import Flask, request
from service.cliente_service import ClienteService
from service.autovettura_service import AutovetturaService
from service.marca_service import MarcaService


# istanziazione applicazione web di tipo Flask
app = Flask(__name__)


# istanziazione componenti Service
cliente_service = ClienteService()
autovettura_service = AutovetturaService()
marca_service = MarcaService()


# **************************** ENDPOINT CLIENTI **************************** #

# endpoint #1: registrazione cliente
# localhost:5000/noleggio/clienti/create
@app.post("/noleggio/clienti/create")
def endpoint_registrazione_cliente():
    corpo_richiesta = request.json
    print(corpo_richiesta)
    return cliente_service.registrazione_cliente(corpo_richiesta)


# endpoint #2: aggiornamento dati cliente
# localhost:5000/noleggio/clienti/update/<id cliente>
@app.put("/noleggio/clienti/update/<int:id>")
def endpoint_aggiornamento_cliente(id):
    corpo_richiesta = request.json
    print(corpo_richiesta, id)
    return cliente_service.aggiornamento_cliente(corpo_richiesta, id)


# endpoint #3: eliminazione cliente
# localhost:5000/noleggio/clienti/delete/<id cliente>
@app.delete("/noleggio/clienti/delete/<int:id>")
def endpoint_eliminazione_cliente(id):
    return cliente_service.eliminazione_cliente(id)


# endpoint #4: dati cliente
# localhost:5000/noleggio/clienti/get/<id cliente>
@app.get("/noleggio/clienti/get/<int:id>")
def endpoint_dati_cliente(id):
    return cliente_service.dati_cliente(id)


# endpoint #5: elenco clienti
# localhost:5000/noleggio/clienti/get
@app.get("/noleggio/clienti/get")
def endpoint_elenco_clienti():
    return cliente_service.elenco_clienti()


# endpoint #6: login cliente
# localhost:5000/noleggio/clienti/login
@app.put("/noleggio/clienti/login")
def endpoint_login_cliente():
    return cliente_service.login_cliente(request.json)


# endpoint #7: logout cliente
# localhost:5000/noleggio/clienti/logout
@app.delete("/noleggio/clienti/logout")
def endpoint_logout_cliente():
    auth_header = request.headers.get("Authorization")
    print(auth_header)
    return cliente_service.logout_cliente(auth_header.split(" ")[1])



# **************************** ENDPOINT AUTOVETTURE **************************** #

# endpoint #1: elenco autovetture
# localhost:5000/noleggio/autovetture/get
@app.get("/noleggio/autovetture/get")
def endpoint_elenco_autovetture():
    return autovettura_service.elenco_autovetture()


# endpoint #2: registrazione autovettura
# localhost:5000/noleggio/autovetture/create
@app.post("/noleggio/autovetture/create")
def endpoint_registrazione_autovettura():
    corpo_richiesta = request.json
    return autovettura_service.registrazione_autovettura(corpo_richiesta)


# **************************** ENDPOINT MARCHE **************************** #

# endpoint #1: elenco marche
# localhost:5000/noleggio/marche/get
@app.get("/noleggio/marche/get")
def endpoint_elenco_marche():
    return marca_service.elenco_marche()








# blocco condizionale di eseguibilità
if __name__ == "__main__":
    app.run()
