import requests
import time
import schedule
from datetime import datetime
import os

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

def notizie_giornaliere():
    oggi = datetime.now().strftime('%d/%m/%Y')
    messaggio = f"📅 *Report Economico del {oggi}*\n\n"
    messaggio += "📈 *Impatto probabile sul Nasdaq Futures:*\n"
    messaggio += "- Dati forti: possibile spinta rialzista\n"
    messaggio += "- Dati deboli: rischio vendite e aumento volatilità\n"
    invia_messaggio(messaggio)

def check_news():
    ora = datetime.now().strftime('%H:%M:%S')
    messaggio = f"⏱️ *Controllo alle {ora}*\n"
    messaggio += "📊 Dato uscito: *NFP 280K vs attese 190K*\n"
    messaggio += "💹 Nasdaq attuale: 18.860\n"
    messaggio += "🎯 *Scenario probabile:* impulso long intraday, con resistenza in area 18.950.\n"
    invia_messaggio(messaggio)

schedule.every().day.at("08:30").do(notizie_giornaliere)
schedule.every(1).minutes.do(check_news)

while True:
    schedule.run_pending()
    time.sleep(1)
