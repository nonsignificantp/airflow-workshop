from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.sql import SQLValueCheckOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

dag = DAG(
    dag_id="postgres-query",
    start_date=datetime(2021, 1, 1),
    end_date=datetime(2021, 2, 1),
    schedule_interval="@daily",
)

t1 = SQLValueCheckOperator(
    task_id="check-data-integrity",
    sql="""
    SELECT COUNT(DISTINCT extract(hour from hora))
    FROM conteo_vehiculos
    WHERE DATE(hora) = '{{ ds }}'
    """,
    pass_value=24,
    conn_id="postgres_default",
    dag=dag,
)

t2 = PostgresOperator(
    task_id="submit-query",
    sql="""
    SELECT COUNT(*)
    FROM conteo_vehiculos
    WHERE DATE(hora) = '{{ ds }}'
    """,
    postgres_conn_id="postgres_default",
    dag=dag,
)

t3 = DummyOperator(
    task_id="exit",
    dag=dag
)

t1 >> t2 >> t3