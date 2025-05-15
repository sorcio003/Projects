import requests
from bs4 import BeautifulSoup
import time

def get_current_time():
    # URL del sito che fornisce l'ora corrente
    url = "https://www.timeanddate.com/worldclock/timezone/utc"

    # Effettua la richiesta GET per ottenere il contenuto della pagina
    response = requests.get(url)

    # Controlla se la richiesta è andata a buon fine (codice di stato HTTP 200)
    if response.status_code == 200:
        # Utilizza BeautifulSoup per analizzare il contenuto HTML della pagina
        soup = BeautifulSoup(response.content, "html.parser")

        # Trova il div con l'ID "ct" che contiene l'orario corrente
        time_div = soup.find(id="ct")

        # Estrai il testo contenuto nel div
        current_time = time_div.get_text(strip=True)

        # Restituisci l'orario corrente
        return current_time
    else:
        print(f"Errore nella richiesta. Codice di stato: {response.status_code}")
        return None

while True:
    # Ottieni l'orario corrente
    current_time = get_current_time()
    
    if current_time:
        # Stampa l'orario corrente
        print("Orario corrente:", current_time)
    
    # Attendi 10 secondi prima di aggiornare di nuovo
    time.sleep(10)
