
# ✅ Connect to Amazon Redshift in Python

This guide shows how to connect to an Amazon Redshift cluster using Python, with examples using both `psycopg2` and `SQLAlchemy`.

---

## 📦 Prerequisites

Install required Python libraries:

```bash
pip install psycopg2-binary sqlalchemy
```

---

## 🔐 Connection Details

Replace these with your actual Redshift cluster details:

```python
REDSHIFT_ENDPOINT = "your-redshift-cluster.endpoint.amazonaws.com"
REDSHIFT_PORT = 5439
REDSHIFT_DB = "bitadb"
REDSHIFT_USER = "adminuser"
REDSHIFT_PASSWORD = "SuperSecret123!"
```

---

## 🐘 Example 1: Using `psycopg2`

```python
import psycopg2

conn = psycopg2.connect(
    dbname=REDSHIFT_DB,
    user=REDSHIFT_USER,
    password=REDSHIFT_PASSWORD,
    host=REDSHIFT_ENDPOINT,
    port=REDSHIFT_PORT
)

cur = conn.cursor()
cur.execute("SELECT current_date;")
result = cur.fetchone()
print("Current Date:", result[0])

cur.close()
conn.close()
```

---

## 🧪 Example 2: Using `SQLAlchemy`

```python
from sqlalchemy import create_engine

engine = create_engine(
    f"postgresql+psycopg2://{REDSHIFT_USER}:{REDSHIFT_PASSWORD}@{REDSHIFT_ENDPOINT}:{REDSHIFT_PORT}/{REDSHIFT_DB}"
)

with engine.connect() as connection:
    result = connection.execute("SELECT version();")
    for row in result:
        print("Redshift Version:", row[0])
```

---

## ✅ Notes

- Redshift uses the PostgreSQL protocol, so `psycopg2` works out of the box.
- Use SQLAlchemy for more complex queries, ORM integration, and Pandas DataFrames.
- Ensure your IP is allowed in the Redshift security group inbound rules (port 5439).

---
