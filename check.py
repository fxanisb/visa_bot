from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
import time

# =========================
# Telegram settings
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
# Chrome settings
# =========================

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 20)

# =========================
# Open mission page
# =========================

driver.get("https://appointment.mosaicvisa.com/mission/4")

wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# =========================
# Click Algiers
# =========================

wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//*[contains(text(),'Algiers')]")
)).click()

# =========================
# Wait calendar page
# =========================

wait.until(EC.url_contains("calendar"))

print("✅ Reached calendar page")
send_telegram("Bot started and checking appointments")

# =========================
# Checking loop
# =========================

while True:
    try:

        print("🔍 Checking appointments...")
        send_telegram("🔄 Bot is checking appointments now")
        
        html = driver.page_source
        found = False

        for number in range(1, 200):
            if f">{number}<" in html:
                print("🚨 Appointment found!")
                send_telegram("🚨 Appointment available in Algiers!")
                found = True
                break

        if not found:
            print("❌ No appointments")

        # wait 50 seconds
        time.sleep(50)

        # reload page
        driver.refresh()

    except Exception as e:
        print("Error:", e)
        time.sleep(50)





