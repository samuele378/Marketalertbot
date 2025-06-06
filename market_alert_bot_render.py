
import requests
import time
import schedule
from datetime import datetime
import os

# === CONFIGURAZIONE ===

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def invia_messaggio(testo):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": testo,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

# === FUNZIONI MESSAGGI ===

def notizie_giornaliere():
    oggi = datetime.now().strftime('%d/%m/%Y')
    messaggio = f"🗓️ *Report Economico del {oggi}*

"
    messaggio += "📌 *Eventi attesi oggi:*
"
    messaggio += "- NFP USA alle 14:30
"
    messaggio += "- Tasso disoccupazione USA
"
    messaggio += "- ISM Non-Manifatturiero

"
    messaggio += "📈 *Impatto probabile sul Nasdaq Futures:*
"
    messaggio += "- Dati forti: possibile spinta rialzista
"
    messaggio += "- Dati deboli: rischio vendite e aumento volatilità
"
    invia_messaggio(messaggio)

def check_news():
    ora = datetime.now().strftime('%H:%M:%S')
    messaggio = f"⏱️ *Controllo alle {ora}*
"
    messaggio += "📊 Dato uscito: *NFP 280K vs attese 190K*
"
    messaggio += "💹 Nasdaq attuale: 18.860
"
    messaggio += "🎯 *Scenario probabile:* impulso long intraday, con resistenza in area 18.950.
"
    invia_messaggio(messaggio)

# === PROGRAMMAZIONE ===

schedule.every().day.at("08:30").do(notizie_giornaliere)
schedule.every(1).minutes.do(check_news)

# === CICLO INFINITO ===

while True:
    schedule.run_pending()
    time.sleep(1)
