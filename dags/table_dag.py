from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG('table_dag', start_date=datetime(2022,1,1), schedule_interval='@daily', catchup=False):
    # define a task to create table using Postgres Operator
    create_table = PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS employees(
                first_name varchar(255) not null,
                last_name varchar(255) not null,
                country varchar(255) not null,
                username varchar(255) not null,
                password varchar(255) not null,
                email varchar(255) not null
            );
        '''
    )

    # task to insert records 
    insert_values = PostgresOperator(
        task_id = 'insert_values',
        postgres_conn_id='postgres',
        sql='''
            INSERT INTO employees (first_name, last_name, country, username, password, email)
            VALUES ('John', 'Doe', 'UK', 'johndoe10', 'pass1','johndoe@example.com'),
            ('Jane', 'Smith', 'USA','johnsmith14', 'pass2', 'janesmith@example.com'),
            ('James', 'Brown', 'USA','jamesbrown12', 'pass3','jamesbrown@example.com');
        '''
    )

    # task to retrieve records
    retrieve_data = PostgresOperator(
        task_id = 'retrieve_data',
        postgres_conn_id='postgres',
        sql='select first_name, email from employees;'
    )

    # set the dependency between the three tasks
    create_table >> insert_values >> retrieve_data
