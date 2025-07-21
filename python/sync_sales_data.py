#!/usr/bin/env python3
"""
sync_sales_data.py
Automates incremental synchronization of sales data from a MySQL staging database
to a PostgreSQL (or IBM DB2) production data warehouse.

Steps:
1. Connects to both MySQL and PostgreSQL databases.
2. Retrieves the latest row ID from the production warehouse.
3. Extracts new records from the staging MySQL instance.
4. Inserts only new rows into the production warehouse.
5. Closes all database connections.
"""

# MySQL connection
import mysql.connector

# PostgreSQL connection
import psycopg2

# --- CONNECT TO MYSQL STAGING DATABASE ---
mysql_conn = mysql.connector.connect(
    user='root',
    password='MyPassword',  # Replace with actual password locally
    host='172.21.219.91',
    database='sales'
)

# --- CONNECT TO POSTGRESQL PRODUCTION DATA WAREHOUSE ---
pg_conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='MyPassword',  # Replace with actual password locally
    host='172.21.114.55',
    port='5432'
)

# --- FETCH LAST ROW ID FROM PRODUCTION WAREHOUSE ---
def get_last_rowid():
    with pg_conn.cursor() as cursor:
        cursor.execute("SELECT MAX(rowid) FROM sales_data")
        result = cursor.fetchone()
        return result[0] if result[0] is not None else 0

last_row_id = get_last_rowid()
print("Last row id on production data warehouse =", last_row_id)

# --- FETCH NEW RECORDS FROM MYSQL STAGING ---
def get_latest_records(rowid):
    with mysql_conn.cursor() as cursor:
        cursor.execute("SELECT * FROM sales_data WHERE rowid > %s", (rowid,))
        return cursor.fetchall()

new_records = get_latest_records(last_row_id)
print("New rows found in staging warehouse =", len(new_records))

# --- INSERT NEW RECORDS INTO PRODUCTION ---
def insert_records(records):
    with pg_conn.cursor() as cursor:
        insert_query = """
        INSERT INTO sales_data(rowid, product_id, customer_id, price, quantity, timestamp)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(insert_query, records)
    pg_conn.commit()

if new_records:
    insert_records(new_records)
    print("New rows inserted into production warehouse =", len(new_records))
else:
    print("No new records to insert.")

# --- CLEANUP ---
mysql_conn.close()
pg_conn.close()
