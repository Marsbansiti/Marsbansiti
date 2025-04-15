
# 🔗 LinkInsight

**LinkInsight** is a Python-based LinkedIn scraping solution that extracts detailed profile and company data efficiently and ethically. It’s ideal for recruiters, lead generators, and analysts who need to collect high-quality LinkedIn data for business use.

---

## 🚀 Features
- Scrapes public LinkedIn profiles and company data (visible without login)
- Extracts structured information using BeautifulSoup
- Export results to CSV or JSON
- Lightweight: uses only Requests + BeautifulSoup
- Ideal for scraping non-authenticated content (e.g., public LinkedIn pages, blog-like pages)

---

## 🧰 Tech Stack
- **Python 3.10+**
- **Requests** – HTTP library for web page access
- **BeautifulSoup** – HTML parsing and data extraction
- **Pandas** – (Optional) for formatting/export

---

## ⚙️ Installation
```bash
pip install requests beautifulsoup4 pandas
```

---

## 🛠️ How to Use
1. Clone the repo:
```bash
git clone https://github.com/yourusername/LinkInsight.git
cd LinkInsight
```

2. Add your list of public LinkedIn URLs in `input.csv`
3. Run the scraper:
```bash
python scrape_bs4.py
```

---

## 🧪 Sample Code (`scrape_bs4.py`)
```python
import requests
from bs4 import BeautifulSoup
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

# Read URLs from input file
with open('input.csv', 'r', encoding='utf-8') as file:
    urls = [line.strip() for line in file.readlines() if line.strip()]

data = []

for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: extract page title
    title = soup.title.string if soup.title else 'N/A'
    data.append([url, title])

# Write to CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['URL', 'Title'])
    writer.writerows(data)
```

---

## 📁 Output Example
| URL                                 | Title                        |
|--------------------------------------|------------------------------|
| linkedin.com/in/sampleuser          | John Smith – LinkedIn       |
| linkedin.com/company/example        | Acme Corp: Overview         |

---

## 📌 Legal & Ethical Notice
This project is intended for educational and ethical data collection purposes only. Always comply with LinkedIn’s [Terms of Service](https://www.linkedin.com/legal/user-agreement) and use responsibly. **Only scrape publicly accessible pages**.

---

## 🤝 Contribute
Want to improve it? Open a pull request or create an issue!

---

## 📬 Contact
If you need a custom version of LinkInsight for your business or project, feel free to reach out at **bitadigitalmarketer@gmail.com**
