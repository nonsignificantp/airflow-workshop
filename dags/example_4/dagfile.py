from airflow.models import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.dummy import DummyOperator
from datetime import datetime

dag = DAG(
    dag_id="testeo-sensor",
    start_date=datetime(2021, 1, 1),
    schedule_interval=None,
)

s1 = FileSensor(
    task_id="wait-for-file",
    filepath="/home/airflow/test",
    poke_interval=5,
    timeout=30,
    dag=dag,
)

t1 = DummyOperator(
    task_id="exit",
    dag=dag,
)

s1 >> t1


