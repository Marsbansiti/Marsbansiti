# 📘 APIs and Data Collection
---

## 🔹 Simple APIs in Python

- Are application programming interfaces.
- Provide straightforward methods for interacting with services, libraries, or data.
- Require minimal configuration or complexity.

## 🔹 General Concepts

- An API lets two pieces of software talk to each other.
- Pandas API processes data by communicating with other software components.
- An instance forms when you create a dictionary and use the DataFrames constructor.
- The `head()` method displays the top rows (default 5).
- The `mean()` method calculates and returns average values.

## 🔹 REST APIs

- Allow internet-based communication to access data, storage, and AI algorithms.
- Transmit data over the internet using HTTP methods.

## 🔹 HTTP and JSON

- HTTP messages often include JSON files with operation instructions.
- These messages are returned as responses from web services.

## 🔹 Time Series & Visualization

- Use Pandas time series functions to work with time-based data.
- Plot daily candlestick charts using Plotly.

## 🔹 HTTP (HyperText Transfer Protocol)

- Transfers data between client (browser) and server over the Web.
- Commonly used in REST API implementations.
- HTTP responses include details like type and length of resource.

## 🔹 URL (Uniform Resource Locator)

- Most common way to locate resources on the Web.
- Structure: Scheme + Internet Address (Base URL) + Route.

## 🔹 HTTP Methods

- `GET`: Retrieve information (can include query strings like name, ID).
- `POST`: Submit data to a server.
- `PUT`: Update existing data.
- `DELETE`: Remove data from the server.
- HTTP responses contain version and body of the response.

## 🔹 Python Requests Library

- Allows sending HTTP/1.1 requests easily.
- Lets you modify results using methods like `GET`.

## 🔹 Web Scraping with Python

- Involves extracting and parsing data from websites.
- Common libraries: Beautiful Soup and requests.

## 🔹 HTML Basics

- Text enclosed in angle-bracket tags.
- HTML documents can include CSS and JavaScript.
- HTML pages resemble trees made of tags and strings.

## 🔹 HTML Tables

- Built with table tags and structured with rows, headers, and body.
- Use `pandas.read_html()` to extract tabular data from web pages.

## 🔹 Beautiful Soup

- Python library to parse and navigate HTML/XML.
- Represents documents as nested data structures (HTML tree).
- Use constructor to get a BeautifulSoup object.
- `NavigableString` behaves like a Python string.
- `find_all()` method:
- - Extracts content by tag name, attributes, or text.
- - Searches through tag’s descendants.
- - Returns a Python iterable (e.g., a list).

## 🔹 File Formats

- Defined by structure and encoding rules (.txt, .csv, .json, .xml, .xlsx, etc.).
- File extensions indicate format and required program.
- Python can handle these formats using libraries like Pandas.

✅ **You’ve learned how APIs work, how to retrieve and manipulate data, and how to use Python tools like `requests`, `Pandas`, and `Beautiful Soup` for real-world data interaction.**
