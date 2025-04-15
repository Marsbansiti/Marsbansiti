# linkedin_scraper_alerts.py
# --------------------------------------------------
# A LinkedIn profile scraper that runs in GitHub Codespaces.
# It scrapes names and headlines from public profiles,
# saves them to a timestamped CSV, and sends a Telegram notification.
# --------------------------------------------------

import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import requests

# --- Load Telegram credentials from environment variables ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# --- Telegram Notification Function ---
def send_telegram(text):
    """
    Sends a message to a Telegram chat using a bot.
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {'chat_id': TELEGRAM_CHAT_ID, 'text': text}
    response = requests.post(url, data=data)
    print("Telegram response:", response.text)

# --- Selenium Setup ---
# Headless mode allows the browser to run in the background
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# --- LinkedIn URLs to Scrape ---
# Add more LinkedIn public profile URLs to this list
urls = [
    "https://www.linkedin.com/in/sampleuser1/",
    "https://www.linkedin.com/in/sampleuser2/"
]

results = []

# --- Generate a timestamped filename for the output CSV ---
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
folder_path = "LinkedIn-Scraping-Projects/LinkAutoScrape/output"
os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
filename = f'{folder_path}/linkedin_results_{timestamp}.csv'

try:
    # --- Loop through each LinkedIn URL ---
    for url in urls:
        driver.get(url)
        time.sleep(5)  # Wait for page to fully load

        try:
            name = driver.find_element(By.TAG_NAME, 'h1').text
        except:
            name = 'N/A'

        try:
            headline = driver.find_element(By.CLASS_NAME, 'text-body-medium').text
        except:
            headline = 'N/A'

        # Save the scraped data to results list
        results.append({
            'URL': url,
            'Name': name,
            'Headline': headline
        })

    # --- Convert results to DataFrame and save to CSV ---
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)

    # --- Send success notification to Telegram ---
    success_message = f"✅ LinkedIn scraper completed successfully!\n📄 File: {filename}\n👥 Profiles scraped: {len(results)}"
    send_telegram(success_message)

except Exception as e:
    # --- Send error notification to Telegram ---
    error_message = f"❌ Scraper failed: {str(e)}"
    send_telegram(error_message)

finally:
    # --- Always close the browser ---
    driver.quit()
