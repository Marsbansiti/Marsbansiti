# 🐍 Cheatsheet: Python Coding Practices and Packaging Concepts
_Estimated time: 5 minutes_
---

## 🔹 Packaging

**📝 Description:**
> Folder structure for creating a package

**💻 Code Example:**
```python
# Folder structure:
project_folder/
└── package_name/
    ├── __init__.py
    ├── module_1.py
    └── module_2.py

# module1.py
def function_1(arg):
    return <operation output>

# __init__.py
from . import function_1
```

## 🔹 Python Style Guide

**📝 Description:**
> Best practices for writing clean Python code

**💻 Code Example:**
```python
# Indentation
def function_1(a, b):
    if a > b:
        c = c + 5
    else:
        c = c - 3
    return c

c = function_1(a, b)

# Constant naming
MAX_FILE_UPLOAD_SIZE
```

## 🔹 Static Code Analysis

**📝 Description:**
> Evaluate code against a style guide without running it

**💻 Code Example:**
```python
# Use Pylint to check code style
pylint code.py
```

## 🔹 Unit Testing

**📝 Description:**
> Write tests to validate individual units of code

**💻 Code Example:**
```python
import unittest
from mypackage.mymodule import my_function

class TestMyFunction(unittest.TestCase):
    def test_my_function(self):
        result = my_function(<args>)
        self.assertEqual(result, <expected_response>)

unittest.main()
```

