set AIRFLOW_VERSION=2.9.0
set PYTHON_VERSION=3.10
set CONSTRAINT_URL=https://raw.githubusercontent.com/apache/airflow/constraints-%AIRFLOW_VERSION%/constraints-%PYTHON_VERSION%.txt

pip install "apache-airflow==%AIRFLOW_VERSION%" --constraint %CONSTRAINT_URL%
