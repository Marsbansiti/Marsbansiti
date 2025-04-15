from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

urls = [
    "https://www.linkedin.com/in/sampleuser1/",
    "https://www.linkedin.com/in/sampleuser2/"
]

results = []

for url in urls:
    driver.get(url)
    time.sleep(5)  # Let it load
    try:
        name = driver.find_element(By.TAG_NAME, 'h1').text
        headline = driver.find_element(By.CLASS_NAME, 'text-body-medium').text
    except:
        name = headline = 'N/A'
    results.append({'URL': url, 'Name': name, 'Headline': headline})

driver.quit()

df = pd.DataFrame(results)
df.to_csv('LinkedIn-Scraping-Projects/LinkAutoScrape/output/linkedin_results.csv', index=False)
