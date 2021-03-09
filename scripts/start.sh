#!/usr/bin/env bash

curl https://gist.githubusercontent.com/tijptjik/9408623/raw/b237fa5848349a14a14e5d4107dc7897c21951f5/wine.csv >> ~/dataset

if [[ ! -f /opt/airflow/airflow.db ]]; then
    airflow db init > /dev/null
fi

airflow users create -u admin -r Admin -p admin -f John -l Admin -e mail@fake.com
airflow scheduler &
exec airflow webserver --host 0.0.0.0 --port 8080