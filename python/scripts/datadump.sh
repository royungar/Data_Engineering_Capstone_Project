#!/bin/bash

# datadump.sh
# Description:
#   Automates the process of exporting the 'sales_data' table from the 'sales' MySQL database.
#   The output is saved into a file named 'sales_data.sql'.
# 
# Notes:
# - Assumes the MySQL server is running and accessible at host 'mysql' on port 3306.
# - Avoid hardcoding passwords in production. Use environment variables or .my.cnf for secure access.
# - This script is intended for development or educational purposes.

# --- Configuration ---
username="root"
password="MyPassword"  # Replace with your actual password when running the script
db_name="sales"
table_name="sales_data"
filename="sales_data.sql"

# --- Dump the table ---
mysqldump --host=mysql --port=3306 --user="$username" --password="$password" "$db_name" "$table_name" > "$filename"

echo "Data export complete: $filename"