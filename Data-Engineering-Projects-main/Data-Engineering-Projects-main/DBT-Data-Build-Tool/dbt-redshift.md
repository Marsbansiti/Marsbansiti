
# ✅ Use Redshift with dbt (Data Build Tool)

This guide helps you quickly set up dbt to work with Amazon Redshift, including:

- `profiles.yml` configuration
- Example dbt model
- Folder structure overview

---

## 📁 Project Structure Overview

```
dbt_project/
├── dbt_project.yml
├── models/
│   └── my_first_model.sql
└── profiles.yml  (in ~/.dbt/)
```

---

## 🧰 Step 1: Configure `profiles.yml` for Redshift

Create or edit `~/.dbt/profiles.yml`:

```yaml
default:
  target: dev
  outputs:
    dev:
      type: redshift
      host: your-redshift-cluster.endpoint.amazonaws.com
      user: adminuser
      password: SuperSecret123!
      port: 5439
      dbname: bitadb
      schema: public
      threads: 1
      ssl: true
```

> 💡 You must place this in the `~/.dbt/` folder on your local machine.

---

## 🛠 Step 2: Initialize Your dbt Project

```bash
dbt init dbt_project
cd dbt_project
```

This creates the necessary project structure.

---

## ✍️ Step 3: Create Your First dbt Model

In the `models/` folder, create a file called `my_first_model.sql`:

```sql
-- models/my_first_model.sql

SELECT
    current_date AS today,
    'Hello from dbt on Redshift!' AS message;
```

---

## 🚀 Step 4: Run dbt Models

```bash
dbt run
```

You’ll see a message indicating successful model creation in your Redshift schema.

---

## ✅ Optional: Run Tests and Docs

```bash
dbt test        # Run schema tests
dbt docs generate && dbt docs serve   # Launch interactive docs
```

---

## 🔒 Security Tips

- Never commit your `profiles.yml` with credentials to version control.
- Use environment variables or secrets manager for production deployments.

---

## 📌 Requirements

- dbt-core (`pip install dbt-core dbt-redshift`)
- IAM role or user with Redshift access
- Proper security group access to port 5439

---

## 📄 Example Use Case

> You want to transform a staging table from S3-loaded data and publish a cleaned version into your `analytics` schema for reporting.

---

Let me know if you'd like a **ready-to-use dbt project ZIP** with:
- Project config
- Example models
- Git-ready structure
