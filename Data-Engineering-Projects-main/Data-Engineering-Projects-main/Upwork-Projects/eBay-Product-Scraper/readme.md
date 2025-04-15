# eBay Product Scraper to Google Sheets + Telegram Notification

This Python script scrapes products from eBay and saves them directly into a **Google Sheets** spreadsheet.  
After the data is added, it also sends a **Telegram message** to notify you.


# 🗺️ Workflow Diagram: eBay Product Scraper Automation

This Markdown file provides a visual representation (in text format) of the automation flow for scraping eBay products, storing them in Google Sheets, and sending a Telegram notification.

---

## 📊 Visual Flow

```
+------------------------+
|  🛒 eBay Search Page    |
|  (source of products)  |
+------------------------+
            |
            v
+---------------------------+
|  🤖 Python Scraper Script  |
|  - Clean & extract data   |
+---------------------------+
            |
            v
+------------------------+
|  📄 Google Sheets       |
|  (store Title, Price,  |
|   and Product Link)    |
+------------------------+
            |
            v
+--------------------------+
|  📬 Telegram Notification |
|  - Sends update to coach |
+--------------------------+
```

---

## 🔤 Labels for Each Block

| Step                | Description                                 |
|---------------------|---------------------------------------------|
| **eBay Search**     | The source of product listings              |
| **Python Scraper**  | A script that scrapes and cleans the data   |
| **Google Sheets**   | Data storage for product details            |
| **Telegram Bot**    | Sends a summary notification to the coach   |

---


## Features
- Scrapes product title, price, and link from eBay search results
- Cleans and standardizes price format
- Stores valid products in Google Sheets
- Sends notification via Telegram Bot to alert about new products

---

## Requirements

Install dependencies with:

```bash
pip install gspread oauth2client beautifulsoup4 requests
```

---

## Setup Instructions

### 1. Create Google Sheet
- Create a sheet titled **eBay Products**
- Make sure the first worksheet has 3 columns: `Title`, `Price`, `Link`

### 2. Enable Google Sheets API
- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project
- Enable **Google Sheets API** and **Google Drive API**
- Create a Service Account and download the `credentials.json` file
- Share your Google Sheet with the Service Account email (e.g., `my-bot@project.iam.gserviceaccount.com`)

Place the `credentials.json` file in the root folder next to your Python script.

---

### 3. Set up Telegram Bot
- Create a bot using [@BotFather](https://t.me/BotFather)
- Get your Bot Token and Chat ID
- Set the following environment variables:

```bash
export TELEGRAM_BOT_TOKEN=your_bot_token
export TELEGRAM_CHAT_ID=your_chat_id
```

---

### 4. Run the Script

```bash
python ebay_to_gsheets_telegram.py
```

---

## Optional: Automate with GitHub Actions or Cron

You can run this script daily using GitHub Actions or a cronjob on your server.

---

No credit card or paid service required. This solution is 100% free and beginner-friendly.


---

# 🛠️ Next Steps (in Codespaces or Locally)

Follow these instructions to get the project running:

1. **Unzip the project**  
   Extract the downloaded `.zip` file to your workspace.

2. **Install dependencies**  
   Make sure Python is installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your `.env` file**  
   Use `.env.example` as a guide to create your actual `.env` file with your Telegram credentials.

4. **Add your `credentials.json` file**  
   Download it from your Google Cloud Console and place it in the project root directory.

5. **Run the script**
   ```bash
   python ebay_to_gsheets_telegram.py
   ```

That's it! Your scraper will send product data to Google Sheets and notify you via Telegram.
