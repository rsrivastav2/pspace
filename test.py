from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def my_task():
    print("Running my task")

with DAG("example_dag",
         start_date=datetime(2024, 1, 1),
         schedule_interval='@daily',
         catchup=False) as dag:

    task = PythonOperator(
        task_id="print_hello",
        python_callable=my_task
    )
