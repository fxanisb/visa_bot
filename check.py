import requests
import time

# =========================
# Telegram Settings
# =========================
TOKEN = "8711953337:AAGsLQ1DgUGnwCKl4-mrcNnQAyLDCoRtw9Y"
CHAT_ID = "5898450345"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

# =========================
# Appointment Checker
# =========================

URL = "https://appointment.mosaicvisa.com/calendar/9"

while True:
    try:
        response = requests.get(URL)
        html = response.text

        print("Checking...")

        # ابحث عن أي رقم أكبر من 0
        found = False

        for number in range(1, 200):
            if f">{number}<" in html:
                send_telegram(f"🔥 Appointment Available! Number found: {number}")
                print("Appointment Found!")
                found = True
                break

        if not found:
            print("No appointments.")

        time.sleep(30)

    except Exception as e:
        print("Error:", e)
        time.sleep(30)




