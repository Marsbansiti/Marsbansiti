#pip install selenium
#pip install -r LinkedIn-Scraping-Projects/LinkAutoScrape/requirements.txt
#pip freeze > requirements.txt


import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

# --- Load secrets from environment variables ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# --- Telegram Notification Function ---
def send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': text}
    response = requests.post(url, data=data)
    print("Telegram response:", response.text)

# --- Selenium Setup ---
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# --- LinkedIn URLs to Scrape ---
urls = [
    "https://www.linkedin.com/in/sampleuser1/",
    "https://www.linkedin.com/in/sampleuser2/"
]

results = []

try:
    for url in urls:
        driver.get(url)
        time.sleep(5)  # wait for page to load

        try:
            name = driver.find_element(By.TAG_NAME, 'h1').text
        except:
            name = 'N/A'

        try:
            headline = driver.find_element(By.CLASS_NAME, 'text-body-medium').text
        except:
            headline = 'N/A'

        results.append({
            'URL': url,
            'Name': name,
            'Headline': headline
        })

    df = pd.DataFrame(results)
    df.to_csv('linkedin_results.csv', index=False)

    send_telegram("✅ LinkedIn scraper completed successfully! CSV generated.")

except Exception as e:
    error_message = f"❌ Scraper failed: {str(e)}"
    send_telegram(error_message)

finally:
    driver.quit()
