# linkedin_scraper_google_sheets.py
# --------------------------------------------------
# A LinkedIn profile scraper that extracts names and headlines
# from public profiles, saves to CSV, and also exports results
# directly to a Google Sheet using gspread.
# --------------------------------------------------

import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# --- Google Sheets Setup ---
# Define the API scopes required for gspread
scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

# Path to your service account credentials JSON file
# Upload this to your Codespaces environment before running
credentials_path = 'credentials.json'

# Authenticate and connect to Google Sheets
creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name (must exist and be shared with service account email)
sheet = client.open("LinkedIn Results").sheet1

# --- Selenium Setup ---
# Configure Selenium to run in headless mode for automation
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# --- LinkedIn URLs to Scrape ---
# Add public profile URLs below
urls = [
    "https://www.linkedin.com/in/sampleuser1/",
    "https://www.linkedin.com/in/sampleuser2/"
]

results = []

# Generate a timestamp for logging and filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
folder_path = "LinkedIn-Scraping-Projects/LinkAutoScrape/output"
os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
filename = f'{folder_path}/linkedin_results_{timestamp}.csv'


try:
    # Loop through each LinkedIn profile URL
    for url in urls:
        driver.get(url)
        time.sleep(5)  # Wait for full page load

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

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)

    # Write header to Google Sheet
    sheet.append_row(["Timestamp", "URL", "Name", "Headline"])

    # Append each profile's result to Google Sheet
    for row in results:
        sheet.append_row([timestamp, row['URL'], row['Name'], row['Headline']])

    print(f"✅ Scraping complete. Results saved to {filename} and uploaded to Google Sheets.")

except Exception as e:
    print(f"❌ An error occurred: {str(e)}")

finally:
    driver.quit()
