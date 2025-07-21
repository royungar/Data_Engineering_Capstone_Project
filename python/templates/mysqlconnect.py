#!/usr/bin/env python3
"""
mysqlconnect.py

A simple script to demonstrate connecting to a MySQL database,
creating a table, inserting sample data, and querying it using Python.

This script uses the mysql-connector-python library.
To install: pip install mysql-connector-python
"""

import mysql.connector

# Replace with your actual MySQL credentials and hostname
MYSQL_USER = 'root'
MYSQL_PASSWORD = '<replace with your MySQL password>'
MYSQL_HOST = '<replace with your MySQL hostname>'
MYSQL_DATABASE = 'sales'

# Connect to the MySQL database
connection = mysql.connector.connect(
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    database=MYSQL_DATABASE
)

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Create a table named 'products' if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS products (
    rowid INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
)
"""
cursor.execute(create_table_query)
print("Table 'products' created or already exists.")

# Insert sample data into the table
insert_data_query = """
INSERT INTO products(product, category)
VALUES
    ("Television", "Electronics"),
    ("Laptop", "Electronics"),
    ("Mobile", "Electronics")
"""
cursor.execute(insert_data_query)
connection.commit()
print("Sample data inserted into 'products'.")

# Query and display the data from the table
select_query = "SELECT * FROM products"
cursor.execute(select_query)

print("Records in 'products' table:")
for row in cursor.fetchall():
    print(row)

# Close the connection to the database
cursor.close()
connection.close()
print("Connection closed.")