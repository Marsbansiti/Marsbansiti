
import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

# Read URLs from input.csv
with open('input.csv', 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file.readlines() if line.strip()]

data = []

for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract page title
    title = soup.title.string if soup.title else 'N/A'
    data.append([url, title])

# Save to output.csv
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Title'])
    writer.writerows(data)