# 🕸️ Web Scraping Project: Top 50 Highly-Ranked Films

## 📌 Overview

Web scraping is used for extracting relevant data from web pages. When data is publicly available on the internet but not directly downloadable, **web scraping** makes the extraction process easier.

In this project, I analyzed the HTML structure of a web page and extracted specific data using **Python web scraping techniques**.

> ✅ **Note:** A basic understanding of HTML elements and tags is essential for successful scraping.

---

## 🎯 Scenario

You have been hired by a **Multiplex Management Organization** to extract data about the **Top 50 movies** with the best average ratings from the following link:

🔗 [Archived Web Page](https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films)

---

## 🎯 Objective

Extract the following information for the top 50 movies:

- 🎬 **Average Rank**
- 🎥 **Film Title**
- 📅 **Year of Release**

---

## 🐍 Python Script

You are required to create a Python script named:

```bash
webscraping_movies.py
```

This script will:

1. Load the web page.
2. Parse the HTML content using `BeautifulSoup`.
3. Locate and extract the top 50 movie entries.
4. Retrieve:
   - Average Rank
   - Film Title
   - Year
5. Save the extracted data to a CSV file:

```bash
top_50_films.csv
```

---

## 💾 Expected Output

A CSV file containing the top 50 films in this format:

| Average Rank | Film Title             | Year |
|--------------|------------------------|------|
| 1            | The Shawshank Redemption | 1994 |
| ...          | ...                    | ...  |

---

## 🛠️ Tools & Libraries

- `requests` – To send an HTTP request to the webpage.
- `BeautifulSoup` – To parse and navigate the HTML content.
- `pandas` – To structure the data and export it as a CSV file.

---

## ✅ Summary

By completing this project, you will have practiced:

- Understanding and analyzing HTML structures.
- Extracting relevant data using Python.
- Automating data collection for real-world applications.
- Saving structured data to a `.csv` file for further use.

