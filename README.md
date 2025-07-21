# Data Engineering Capstone Project – IBM Professional Certificate

##  Overview

This capstone project simulates the role of a Data Engineer at **SoftCart**, an e-commerce company with global reach. The project integrates OLTP and NoSQL systems, a PostgreSQL data warehouse, ETL pipelines, a BI dashboard, and Spark-based machine learning. It was completed as part of the [IBM Data Engineering Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-engineer) on Coursera.

![Data Platform Architecture](images/data-platform-architecture.png)
---

##  Objectives

- Design and implement a complete data platform for SoftCart
- Build OLTP and NoSQL databases for operational data
- Design a star-schema data warehouse and load data into it
- Automate ETL pipelines for incremental data loads
- Create a BI dashboard using IBM Cognos Analytics
- Perform search analytics and sales prediction using Apache Spark

---

##  Tools & Technologies

| Category           | Tools/Technologies                                                    |
|--------------------|-----------------------------------------------------------------------|
| **Databases**      | MySQL, MongoDB, PostgreSQL                                            |
| **ETL & Automation** | Bash, Python (`mysql-connector-python`, `psycopg2`), Apache Airflow |
| **Data Warehouse** | PostgreSQL (staging), IBM Db2 (production - simulated locally)        |
| **Big Data & ML**  | Apache Spark, PySpark, Spark MLlib                                    |
| **Visualization**  | IBM Cognos Analytics                                                  |

---

## Project Modules & Components

### Module 1: OLTP Database (MySQL)
- Created `sales_data` table and populated it with `oltpdata.csv`
- Set up an index on the `timestamp` field
- Automated export of the data using a Bash script

Files:
- `sql/sales_module1.sql`
- `data/oltpdata.csv`
- `python/scripts/datadump.sh`

---

### Module 2: NoSQL Catalog (MongoDB)
- Imported catalog data from `catalog.json` into MongoDB
- Created indexes and executed aggregation queries
- Exported selected fields into CSV

Files:
- `data/catalog.json`
- `mongodb/module2_mongodb_commands.txt`

---

### Module 3: Data Warehouse Design & Queries (PostgreSQL)
- Designed and implemented a star schema with fact/dimension tables
- Loaded data from CSVs into staging PostgreSQL
- Performed advanced aggregation: `ROLLUP`, `CUBE`, `GROUPING SETS`, and materialized views

Files:
- `sql/warehouse_schema.sql` – ERD schema creation
- `sql/create_script_module3_given.sql` – Provided setup script
- `sql/aggregation_queries_module3_part2.sql` – Aggregation queries
- `data/DimDate.csv`, `DimCategory.csv`, `DimCountry.csv`, `FactSales.csv`

---

### Module 4: Business Intelligence Dashboard (IBM Cognos)
- Created a BI dashboard with:
  - Line chart: Total monthly sales for 2020
  - Pie chart: Category-wise sales for 2020
  - Bar chart: Quarterly mobile phone sales

Files:
- `dashboards/total-sales-per-month-in-2020.png` - Screenshots of the dashboard visuals
- `dashboards/total-sales-per-category-in-2020.png`
- `dashboards/quarterly-sales-of-mobile-phones.png`

---

### Module 5: ETL Pipelines
- Modified and executed `sync_sales_data.py` to sync new rows from MySQL → PostgreSQL
- Created Airflow DAG `process_web_log.py` to extract, transform, and load log data

Files:
- `data/sales.csv`, `data/sales_dump_module5.sql`
- `python/sync_sales_data.py` – Final ETL script
- `python/templates/mysqlconnect.py`, `postgresqlconnect.py` – Connection templates
- `airflow/process_web_log.py` – DAG script

---

### Module 6: Spark ML for Sales Forecasting
- Ingested `searchterms.csv` using PySpark
- Ran frequency and search-term analytics
- Loaded a pretrained Spark ML model and predicted sales for 2023

Files:
- `sparkml/Spark_MLOps.ipynb`
- `sparkml/searchterms.csv`
- `sparkml/sales_prediction.model/` – Trained model folder

---

## Repository Structure

```plaintext
Data_Engineering_Capstone_Project/
├── README.md                                  # Project overview and instructions
├── airflow/
│   └── process_web_log.py                     # Airflow DAG for processing web logs
├── dashboards/                                # Cognos dashboard screenshots
│   ├── total-sales-per-month-in-2020.png
│   ├── total-sales-per-category-in-2020.png
│   └── quarterly-sales-of-mobile-phones.png 
├── data/
│   ├── oltpdata.csv                           # Input file for OLTP (Module 1)
│   ├── sales.csv                              # MySQL sales staging data (Module 5)
│   ├── sales_data.sql                         # SQL dump of sales_data table from MySQL (via datadump.sh)
│   ├── sales_dump_module5.sql                 # Provided SQL dump for MySQL setup (Module 5)
│   ├── catalog.json                           # JSON data to be imported into MongoDB (Module 2)
│   ├── ecommerce.csv                          # Input for Spark ML (Module 4)
│   ├── accesslog.txt                          # Raw web log file used in Airflow DAG (Module 5)
│   ├── DimDate.csv                            # Data warehouse dimension tables (Module 3)
│   ├── DimCategory.csv
│   ├── DimCountry.csv
│   ├── FactSales.csv
├── images/
│   └── data-platform-architecture.png         # Architecture diagram used in README
├── mongodb/
│   └── module2_mongodb_commands.txt           # MongoDB shell commands for catalog import and analysis
├── python/
│   ├── sync_sales_data.py                     # Python ETL script for incremental sync from MySQL to PostgreSQL
│   ├── scripts/
│   │   └── datadump.sh                        # Bash script to export MySQL data
│   └── templates/
│       ├── mysqlconnect.py                    # Sample connection and setup for MySQL (provided template)
│       └── postgresqlconnect.py               # Sample connection and setup for PostgreSQL (provided template)
├── sparkml/
│   ├── Spark_MLOps.ipynb                      # PySpark notebook: ingest, train, and evaluate sales prediction model
│   ├── searchterms.csv                        # Input dataset for Spark ML pipeline
│   └── sales_prediction.model/                # Saved trained model and metadata
├── sql/
│   ├── sales_module1.sql                      # OLTP schema and operations (Module 1)
│   ├── warehouse_schema.sql                   # Data warehouse schema (custom ERD version)
│   ├── create_script_module3_given.sql        # Provided CREATE TABLE script (Module 3)
│   └── aggregation_queries_module3_part2.sql  # ROLLUP, CUBE, GROUPING SETS, MQT (Module 3)
```

---

## How to Run Locally

> Note: Some functionality (e.g., Cognos Analytics) is cloud-based or part of IBM Skills Network Labs. Adapt steps as needed for your local environment.

1. **OLTP Setup:**
   - Load `oltpdata.csv` into MySQL.
   - Run `sales_module1.sql` and `datadump.sh`.

2. **NoSQL Setup:**
   - Use `module2_mongodb_commands.txt` to import and query `catalog.json`.

3. **Data Warehouse:**
   - Run `warehouse_schema.sql` or `create_script_module3_given.sql` on PostgreSQL.
   - Load CSVs into the appropriate tables.

4. **ETL Pipeline:**
   - Run `sync_sales_data.py` to insert incremental rows.
   - Execute `process_web_log.py` DAG in Apache Airflow.

5. **Spark ML:**
   - Open `Spark_MLOps.ipynb`, ingest `searchterms.csv`, and load the model to generate predictions.

---

## License

This project was completed as part of the IBM Data Engineering Professional Certificate and is intended for educational use.

## Links

Data Engineering Capstone Project - (https://www.coursera.org/learn/data-enginering-capstone-project)
GitHub Repository - (https://github.com/royungar)