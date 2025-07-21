# postgresqlconnect.py
# Requires: psycopg2
# Install using: python3 -m pip install psycopg2

import psycopg2

# --- Connection Details ---
dsn_hostname = '<replace with your postgres hostname>'
dsn_user = 'postgres'
dsn_pwd = '<replace with your postgres password>'
dsn_port = '5432'
dsn_database = 'postgres'

# --- Establish Connection ---
conn = psycopg2.connect(
    database=dsn_database,
    user=dsn_user,
    password=dsn_pwd,
    host=dsn_hostname,
    port=dsn_port
)

# --- Create Cursor Object ---
cursor = conn.cursor()

# --- Create Table ---
create_table_sql = """
CREATE TABLE IF NOT EXISTS products (
    rowid INTEGER PRIMARY KEY NOT NULL,
    product VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
)
"""
cursor.execute(create_table_sql)
print("Table created.")

# --- Insert Records (Manually) ---
cursor.execute("INSERT INTO products (rowid, product, category) VALUES (1, 'Television', 'Electronics')")
cursor.execute("INSERT INTO products (rowid, product, category) VALUES (2, 'Laptop', 'Electronics')")
cursor.execute("INSERT INTO products (rowid, product, category) VALUES (3, 'Mobile', 'Electronics')")
conn.commit()

# --- Insert List of Records (Batch) ---
list_of_records = [
    (4, 'Tablet', 'Electronics'),
    (5, 'Headphones', 'Electronics')
]

insert_sql = "INSERT INTO products (rowid, product, category) VALUES (%s, %s, %s)"
cursor.executemany(insert_sql, list_of_records)
conn.commit()

# --- Query Data ---
cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

# --- Close Connection ---
cursor.close()
conn.close()

# --- Print Retrieved Records ---
for row in rows:
    print(row)