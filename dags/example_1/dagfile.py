from airflow.models.dag import DAG
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
from random import random

# Definir dag y sus parametros
dag = DAG(
    dag_id="estructura",
    start_date=datetime(2021, 1, 1),
    schedule_interval=None,
)

def rbranch():
    if random() > .5:
        return "exit"
    return ["task1", "task2"]

# Definir las tareas y sus paremetros
t1 = BranchPythonOperator(
    task_id="entry",
    python_callable=rbranch,
    dag=dag
)

t2 = DummyOperator(
    task_id="task1",
    dag=dag
)

t3 = DummyOperator(
    task_id="task2",
    dag=dag
)

t4 = DummyOperator(
    task_id="exit",
    trigger_rule="all_done",
    dag=dag
)

# interconectar las tareas
t1 >> [t2, t3] >> t4
t1 >> t4