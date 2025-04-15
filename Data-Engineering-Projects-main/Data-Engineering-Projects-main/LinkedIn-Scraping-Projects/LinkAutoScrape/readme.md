# 🔗 LinkAutoScrape – Cloud-Based LinkedIn Scraper

A GitHub Codespaces-powered LinkedIn scraper that extracts profile data using Selenium, automates runs using GitHub Actions, and sends real-time notifications via Telegram or Mailgun.

![Scraper Run Status](https://img.shields.io/github/actions/workflow/status/bashoori/Data-Engineering-Projects/scrape.yml?label=Scraper%20Run&logo=github)
![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)
![Automation](https://img.shields.io/badge/Automation-GitHub%20Actions-blue?logo=githubactions)

---

## 📸 Sample Output
![Sample Output CSV](https://github.com/bashoori/Data-Engineering-Projects/raw/main/LinkedIn-Scraping-Projects/LinkAutoScrape/assets/sample-output.png)

> The scraper creates a clean `linkedin_results.csv` file with name, headline, and more (extendable).


---

# 📄 LinkedIn Profile Scraper

A cloud-based Python automation project that scrapes LinkedIn profile information using **Selenium**, runs entirely in **GitHub Codespaces**, and is scheduled to execute daily using **GitHub Actions**. Scraped data is saved in a structured CSV file for analysis, reporting, or integration with Google Sheets.

---

## 🛠 Features
- ✅ Headless scraping of LinkedIn profiles (no UI needed)
- ✅ Automated scheduled runs via GitHub Actions
- ✅ CSV export of profile data
- ✅ Notification via Telegram or Mailgun
- ✅ Works fully in the cloud (no local setup required)

---

## 🧰 Tech Stack
- Python 3.10+
- Selenium (Chrome WebDriver)
- Pandas (for CSV export)
- GitHub Codespaces
- GitHub Actions (for scheduling)

---

## 📁 Project Structure
```
linkedin-scraper/
├── .github/
│   └── workflows/
│       └── scrape.yml
├── scraper.py
├── requirements.txt
└── linkedin_results.csv (output)
```

---


## 📁 Files Included
- `scraper.py` – Main scraper logic
- `scraper_with_telegram.py` – Sends Telegram alerts
- `.github/workflows/scrape.yml` – CI/CD config for daily runs
- `linkedin_results.csv` – Output file sample
- `Mailgun_Email_Notification_Setup.md`
- `Telegram_Notification_Setup.md`
- `Output_Automation_Enhancements.md`

---

## 💡 How to Run
1. Open in GitHub Codespaces or clone locally
2. Install dependencies
3. Replace placeholder URLs and tokens
4. Run the script or trigger via GitHub Actions

---

> 📌 A simple but powerful example of real-world scraping + automation!
