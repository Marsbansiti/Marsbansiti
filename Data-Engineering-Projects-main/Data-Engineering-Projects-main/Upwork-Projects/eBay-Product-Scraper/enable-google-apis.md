# ✅ How to Enable Google Sheets API & Google Drive API

This guide walks you through enabling the necessary Google APIs and setting up a service account to connect with your Python scripts or automation tools.

---

## 🔹 Step 1: Go to Google Cloud Console
👉 Visit: [https://console.cloud.google.com/](https://console.cloud.google.com/)

---

## 🔹 Step 2: Create or Select a Project
- Click the project dropdown (top of the page)
- Choose an existing project or:
  1. Click **“New Project”**
  2. Enter a name
  3. Click **Create**

---

## 🔹 Step 3: Enable Google Sheets API
1. In the left menu, go to: `APIs & Services > Library`
2. Search for **Google Sheets API**
3. Click the result
4. Click **Enable**

---

## 🔹 Step 4: Enable Google Drive API
1. Still in the API Library, search for **Google Drive API**
2. Click the result
3. Click **Enable**

---

## 🔹 Step 5: Create a Service Account
1. In the left menu, go to: `IAM & Admin > Service Accounts`
2. Click **“+ Create Service Account”**
3. Enter a name and description (e.g. `sheets-bot`)
4. Click **Create and Continue**
5. Grant role: choose **Editor** (or minimal required access)
6. Click **Done**

---

## 🔹 Step 6: Create and Download Credentials
1. Open the newly created service account
2. Go to the **“Keys”** tab
3. Click **“Add Key” > “Create New Key”**
4. Choose **JSON** → Click **Create**
5. Save the downloaded file `credentials.json`

---

## 🔹 Step 7: Share Your Google Sheet
1. Open the Google Sheet you want to use
2. Click **“Share”**
3. Add the **client email** from your `credentials.json` file (e.g. `my-bot@your-project.iam.gserviceaccount.com`)
4. Give it **Editor** access

---

✅ Done! Your service account can now access your Google Sheet using the Sheets API.

You can now use this setup in Python with `gspread`, or in platforms like Make.com, Zapier, or Google Apps Script.
