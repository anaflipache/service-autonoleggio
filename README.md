# 🚗 Service Autonoleggio

**Service Autonoleggio** è un'applicazione backend in Python progettata per gestire un sistema di autonoleggio. Espone API dedicate alla gestione di clienti, veicoli e marche, consentendo funzionalità per il monitoraggio e la gestione completa delle operazioni legate al noleggio di veicoli.


## 💡 Funzionalità

- **Gestione dei veicoli**: Inserimento, modifica e cancellazione di veicoli disponibili per il noleggio.
- **Gestione dei clienti**: Registrazione e gestione delle informazioni dei clienti.
- **Gestione delle prenotazioni**: Creazione e monitoraggio delle prenotazioni effettuate dai clienti.
  

## 🔹 Endpoints disponibili

### Endpoint #1 – 👥 Clienti

- **Registrazione cliente**  
  `POST /noleggio/clienti/create`  
  Registra un nuovo cliente.

- **Aggiornamento dati cliente**  
  `PUT /noleggio/clienti/update/<id>`  
  Modifica i dati di un cliente esistente.

- **Eliminazione cliente**  
  `DELETE /noleggio/clienti/delete/<id>`  
  Elimina un cliente specifico.

- **Dati cliente**  
  `GET /noleggio/clienti/get/<id>`  
  Restituisce le informazioni di un cliente.

- **Elenco clienti**  
  `GET /noleggio/clienti/get`  
  Restituisce tutti i clienti registrati.

- **Login cliente**  
  `PUT /noleggio/clienti/login`  
  Effettua il login di un cliente.

- **Logout cliente**  
  `DELETE /noleggio/clienti/logout`  
  Effettua il logout del cliente tramite token.

---

### Endpoint #2 – 🚘 Autovetture

- **Elenco autovetture**  
  `GET /noleggio/autovetture/get`  
  Restituisce tutte le autovetture registrate.

- **Registrazione autovettura**  
  `POST /noleggio/autovetture/create`  
  Aggiunge una nuova autovettura.

---

### Endpoint #4 – 🏷️ Marche

- **Elenco marche**  
  `GET /noleggio/marche/get`  
  Restituisce la lista delle marche auto disponibili.

---


## 📌 Tecnologie utilizzate

- **Python**: backend
- **Flask** – framework per la creazione dell’API 
- **MySQL** – database relazionale
- **JSON** – formato di scambio dati
