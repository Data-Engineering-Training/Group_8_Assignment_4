from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import csv
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 29),
    'retries': 1,
}

# Define the directory where the CSV file is located
csv_directory = os.path.join(os.path.dirname(__file__), 'data_generation')

def ingest_data_to_postgres():
    # Construct the path to the CSV file
    csv_file_path = os.path.join(csv_directory, 'kasapreko_data.csv')

    # Read data from CSV and ingest into PostgreSQL
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Insert row into PostgreSQL
            # Use PostgresHook to execute SQL queries
            pg_hook = PostgresHook(postgres_conn_id='postgres_default')
            connection = pg_hook.get_conn()
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO Kasapreko (Name, Address, Transaction_Amount, Transaction_Date, Customer_Preference, Product, Product_Quantity)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                row['Name'], row['Address'], row['Transaction Amount'], row['Transaction Date'],
                row['Customer Preference'], row['Product'], row['Product Quantity']
            ))
            connection.commit()
            cursor.close()
            connection.close()

with DAG('data_ingestion_dag', default_args=default_args, schedule_interval='@daily') as dag:
    ingest_data_task = PythonOperator(
        task_id='ingest_data_to_postgres',
        python_callable=ingest_data_to_postgres,
    )
