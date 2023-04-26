from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

# Create a DAG with a specified DAG ID, start date, schedule interval, and catch-up option
with DAG('dag1', start_date=datetime(2022,1,1), schedule_interval='@daily', catchup=False):
    # Task to create a table in Postgres
    create_table = PostgresOperator(
        task_id = 'create_table',
        postgres_conn_id='postgres',  # Postgres connection ID
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

    # Task to insert values into the employees table in Postgres
    insert_values = PostgresOperator(
        task_id = 'insert_values',
        postgres_conn_id='postgres',  # Postgres connection ID
        sql='''
            INSERT INTO employees (first_name, last_name, country, username, password, email)
            VALUES ('John', 'Doe', 'UK', 'johndoe10', 'pass1','johndoe@example.com'),
            ('Jane', 'Smith', 'USA','johnsmith14', 'pass2', 'janesmith@example.com'),
            ('James', 'Brown', 'USA','jamesbrown12', 'pass3','jamesbrown@example.com');
        '''
    )

    # Task to retrieve data from the employees table in Postgres
    retrieve_data = PostgresOperator(
        task_id = 'retrieve_data',
        postgres_conn_id='postgres',  # Postgres connection ID
        sql='select first_name, email from employees;'  # SQL query to retrieve data
    )
