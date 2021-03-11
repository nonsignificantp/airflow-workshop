# Airflow Workshop

## Instrucciones

Para utilizar el repositorio necesitamos tener `docker` y `make` instalado. Una vez parados en el la carpeta raiz del proyecto ejecutamos:

```
make airflow
```

En caso de no tener `make` se puede ejecutar el container directamente con la siguiente instruccion:

```
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
```

Una vez levantado el ambiente de docker podemos ingresar por el navegador a travez de la direccion [http://localhost:8080/](http://localhost:8080/) con el usuario `admin` y el password `admin`.

