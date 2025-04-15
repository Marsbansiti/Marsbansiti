# API Retry with Exponential Backoff

This project demonstrates a simple yet robust Python function for fetching data from an API using **retry logic with exponential backoff**. It’s ideal for use in data pipelines or any situation where external APIs may intermittently fail due to timeouts or rate limits.

## 🔍 Features

- Automatically retries failed API requests
- Implements exponential backoff to reduce load on servers
- Handles common HTTP exceptions gracefully
- Logs attempts and outcomes for better monitoring

## 📘 Use Case

Imagine you're pulling data from a public API as part of a daily ETL job. Sometimes the API fails due to server errors or slow response. This script ensures your pipeline doesn't break immediately and tries to recover by retrying with increasing delay.

## 📁 File Structure
```python
api-retry-backoff/
│
├── fetch_data.py        # Core retry logic script
├── README.md            # Project description and usage
└── requirements.txt     # Python dependencies
```

## 🧪 Example

```python
from fetch_data import fetch_data_with_retry

data = fetch_data_with_retry("https://api.example.com/data")

if data:
    print("Data retrieved successfully!")
else:
    print("Failed to retrieve data.")
```



