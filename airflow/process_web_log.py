#!/usr/bin/env python3
"""
Airflow DAG: process_web_log
Description:
    A simple ETL pipeline that extracts IP addresses from a web server log,
    filters out a specific IP, and archives the result daily.
Author: Roy Ungar
"""

from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email import EmailOperator  # Note: Only imported, not used in this DAG
from airflow.utils.dates import days_ago

# Default arguments applied to all tasks
default_args = {
    'owner': 'Roy',
    'start_date': days_ago(1),                # Start running DAG from yesterday
    'email': ['someemail@gmail.com'],         # Notification email on failure/retry
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,                              # Retry once if a task fails
    'retry_delay': timedelta(minutes=5),       # Wait 5 minutes before retrying
}

# Define the DAG
dag = DAG(
    'process_web_log',
    description='DAG to process web server logs daily',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Run once every day
    catchup=False
)

# Task 1: Extract IP addresses from access log
extract_data = BashOperator(
    task_id='extract_data',
    bash_command=(
        "cut -d' ' -f1 /home/project/airflow/dags/capstone/accesslog.txt > "
        "/home/project/airflow/dags/capstone/extracted_data.txt"
    ),
    dag=dag
)

# Task 2: Transform data by removing a specific IP address
transform_data = BashOperator(
    task_id='transform_data',
    bash_command=(
        "grep -v '198.46.149.143' /home/project/airflow/dags/capstone/extracted_data.txt > "
        "/home/project/airflow/dags/capstone/transformed_data.txt"
    ),
    dag=dag
)

# Task 3: Load transformed data by compressing it into a .tar archive
load_data = BashOperator(
    task_id='load_data',
    bash_command=(
        "tar -cf /home/project/airflow/dags/capstone/weblog.tar "
        "/home/project/airflow/dags/capstone/transformed_data.txt"
    ),
    dag=dag
)

# Set task execution order
extract_data >> transform_data >> load_data