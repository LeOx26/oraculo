from urllib import request
import requests
from datetime import datetime
from airflow import DAG
from airflow.decorators import task
from stock_data import data


DAG(dag_id='list_acciones screener',
schedule=None,
start_date=datetime(2020,10,10),
tags=['task']
)



