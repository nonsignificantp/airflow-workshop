airflow:
	docker run \
		-it --rm \
		--entrypoint bash \
		-v ${PWD}/dags:/opt/airflow/dags \
		-v ${PWD}/scripts:/scripts \
		-p 8080:8080 \
		-e AIRFLOW__SCHEDULER__DAG_DIR_LIST_INTERVAL=10 \
		-e AIRFLOW__WEBSERVER__EXPOSE_CONFIG=True \
		apache/airflow:2.0.0-python3.6 \
		/scripts/start.sh
		