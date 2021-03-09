"""
# Este es mi dag
Bienvenidos a mi dag.
"""

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.microsoft.azure.transfers.file_to_wasb import FileToWasbOperator
from datetime import datetime

dag = DAG(
    dag_id="local-to-azure",
    start_date=datetime(2021,1,1),
    end_date=datetime(2021, 2, 1),
    schedule_interval="@daily",
    tags=["gcdd", "diaria"]
)

dag.doc_md = __doc__

t1 = BashOperator(
    task_id="download-data",
    bash_command="cp ~/dataset ~/{{ ds }}",
    dag=dag
)

t2 = FileToWasbOperator(
    task_id="upload-to-azure",
    container_name="public",
    file_path="/home/airflow/{{ ds }}",
    blob_name="airflow/{{ ds }}",
    wasb_conn_id="wasb_default",
    dag=dag
)

t3 = BashOperator(
    task_id="remove-data",
    bash_command="rm ~/{{ ds }}",
    dag=dag
)

t1 >> t2 >> t3

