from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.bash import BashOperator

import json
from pandas import json_normalize
import pandas as pd

filePath = '/opt/airflow/csv_files/user_processed.csv'
comma = ','

def _process_user(ti):
    res = ti.xcom_pull(task_ids='extract_user')
    user = res['results'][0]

    processed_user = json_normalize({
        'first_name': user['name']['first'],
        'last_name': user['name']['last'],
        'country':user['location']['country'],
        'email':user['email'],
        'username':user['login']['username'],
        'password':user['login']['password']
    })
    processed_user.to_csv('/opt/airflow/csv_files/user_processed.csv',index=None, header=False)


# def _store_user():
#     hook = PostgresHook(postgres_conn_id = 'postgres')
#     hook.copy_expert(
#         sql="copy users from stdin DELIMITER as ','",
#         filename='/tmp/processed_user.csv'
#     )
    



with DAG('user_processing', start_date=datetime(2022,1,1), schedule_interval='@daily', catchup=False) as dag:
    create_table = PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id= 'postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS users(
                first_name varchar(255) not null,
                last_name varchar(255) not null,
                country varchar(255) not null,
                username varchar(255) not null,
                password varchar(255) not null,
                email varchar(255) not null
            );
        '''
    )    

    is_api_available = HttpSensor(
        task_id='is_api_available',
        http_conn_id='user_api',
        endpoint= 'api/'
    )

# user extracted is pushed in xcoms, from where we are pulling it in process_user task
    extract_user = SimpleHttpOperator(
        task_id='extract_user',
        http_conn_id='user_api',
        endpoint='api/',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

# process_user needs xcoms which comes from the extract_user, Hence specyfying dependency is important otherwise they will be executed at the same time
    process_user = PythonOperator(
        task_id = 'process_user',
        python_callable=_process_user
    )

    # copy_task = PythonOperator(
    #     task_id = 'copy_task',
    #     python_callable=_store_user
    # )

    copy_task = PostgresOperator(
        task_id = 'copy_task',
        postgres_conn_id='postgres',
        sql='''COPY users(first_name, last_name,country, username, password, email) FROM '/opt/airflow/csv_files/user_processed.csv' delimiter ',' CSV'''
    )


    create_table >> is_api_available >> extract_user >> process_user >> copy_task



# create table to store users --> PostgresOperator
# check if api is available --> HttpSensor
# extract user by making an api request --> SimpleHttpOperator(for making api request)
# process the user and save it in a csv file -> PythonOperator
# Store the user saved in the file into the table --> PostgressHook.copy_expert method to copy the record from csv file to table




