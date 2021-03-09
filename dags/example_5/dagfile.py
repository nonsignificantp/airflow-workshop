from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime
from random import random

conf = {
    "retries":5,
    "retry_delay":1,
}

def rfail():
    if random() > .2:
        raise ValueError("Esto es un error")

with DAG(dag_id="ultimo-dag", start_date=datetime(2021, 1, 1), schedule_interval=None, default_args=conf) as dag:
    t1 = DummyOperator(task_id="entry")

    with TaskGroup("group1") as g1:
        t2 = PythonOperator(task_id="task1", python_callable=rfail)
        t3 = PythonOperator(task_id="task2", python_callable=rfail)
        t4 = PythonOperator(task_id="task3", python_callable=rfail)

t1 >> g1