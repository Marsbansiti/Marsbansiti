# 📘 Cheat Sheet: APIs and Data Collection
---

## 🔹 Accessing element attribute

**📝 Description:**
> Access the value of a specific attribute of an HTML element

**💻 Code Example:**
```python
attribute = element["attribute"]
```

## 🔹 BeautifulSoup()

**📝 Description:**
> Parse the HTML content using BeautifulSoup

**💻 Code Example:**
```python
soup = BeautifulSoup(html, "html.parser")
```

## 🔹 delete()

**📝 Description:**
> Send a DELETE request to remove a resource

**💻 Code Example:**
```python
response = requests.delete(url)
```

## 🔹 find()

**📝 Description:**
> Find the first HTML element matching the tag and attributes

**💻 Code Example:**
```python
element = soup.find(tag, attrs)
```

## 🔹 find_all()

**📝 Description:**
> Find all HTML elements matching the tag and attributes

**💻 Code Example:**
```python
elements = soup.find_all(tag, attrs)
```

## 🔹 findChildren()

**📝 Description:**
> Find all child elements of an HTML element

**💻 Code Example:**
```python
children = element.findChildren()
```

## 🔹 get()

**📝 Description:**
> Perform a GET request to retrieve data

**💻 Code Example:**
```python
response = requests.get(url)
```

## 🔹 Headers

**📝 Description:**
> Include custom headers in the request

**💻 Code Example:**
```python
headers = {"Authorization": "Bearer YOUR_TOKEN"}
```

## 🔹 Import Libraries

**📝 Description:**
> Import necessary Python libraries for web scraping

**💻 Code Example:**
```python
from bs4 import BeautifulSoup
```

## 🔹 json()

**📝 Description:**
> Parse JSON data from response

**💻 Code Example:**
```python
data = response.json()
```

## 🔹 next_sibling()

**📝 Description:**
> Find the next sibling element in the DOM

**💻 Code Example:**
```python
sibling = element.find_next_sibling()
```

## 🔹 parent

**📝 Description:**
> Access the parent element in the DOM

**💻 Code Example:**
```python
parent = element.parent
```

## 🔹 post()

**📝 Description:**
> Send a POST request to submit data

**💻 Code Example:**
```python
response = requests.post(url, data={"key": "value"})
```

## 🔹 put()

**📝 Description:**
> Send a PUT request to update data

**💻 Code Example:**
```python
response = requests.put(url, data={"key": "value"})
```

## 🔹 Query parameters

**📝 Description:**
> Pass query parameters in the URL

**💻 Code Example:**
```python
params = {"page": 1, "per_page": 10}
```

## 🔹 select()

**📝 Description:**
> Select HTML elements using CSS selector

**💻 Code Example:**
```python
element = soup.select("selector")
```

## 🔹 status_code

**📝 Description:**
> Check HTTP status code of response

**💻 Code Example:**
```python
status_code = response.status_code
```

## 🔹 tags for find()/find_all()

**📝 Description:**
> Specify valid HTML tags to search elements

**💻 Code Example:**
```python
(a), (p), (h1-h6), (table), (tr), (td), (th), (img), (form), (button)
```

## 🔹 text

**📝 Description:**
> Retrieve the text content of an HTML element

**💻 Code Example:**
```python
text = element.text
```

