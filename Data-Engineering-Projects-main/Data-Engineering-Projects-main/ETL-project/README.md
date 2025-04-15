# 📊 Extract, Transform, and Load (ETL) Process for Data Engineers

The **ETL (Extract, Transform, Load)** process is a core responsibility of a **Data Engineer**. It involves gathering data from various sources, applying transformations to clean or format the data, and finally loading it into a data store for analysis or further processing.

This document outlines the objectives and provides a step-by-step guide to begin working with common file formats used in ETL workflows.

---

## 🎯 Objectives

As part of this exercise, you will:

1. 📥 **Read** data from the following file types:
   - CSV
   - JSON
   - XML
2. 🔍 **Extract** the required data from each file type.
3. 🔄 **Transform** the data to match a target schema or format.
4. 💾 **Load** the transformed data into a format ready for storage in a **Relational Database Management System (RDBMS)**.

---

## 📦 Download the Data

You’ll work with a dataset provided in multiple file formats. Download and extract the contents using the commands below:

```bash
# Step 1: Download the source data zip file
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip

# Step 2: Unzip the downloaded file
unzip source.zip

This will extract files in .csv, .json, and .xml formats, which you can use for ETL practice.

💡 Tip: Make sure you have the required libraries installed in your Python environment (like pandas, xml.etree.ElementTree, or json) to work with these file formats.