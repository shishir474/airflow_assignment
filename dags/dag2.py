from airflow import DAG
from datetime import datetime
from airflow.operators.email import EmailOperator
from airflow.operators.python import PythonOperator

# Define a Python function to be called by the PythonOperator task
def printHello():
    print('hello world')

# Create a DAG with a specified DAG ID, start date, schedule interval, and catch-up option
with DAG('dag2', start_date=datetime(2022,1,1), schedule_interval='@daily', catchup=False):
    # Task to call the printHello function using PythonOperator
    dummy_task = PythonOperator(
        task_id = 'dummy_task',
        python_callable=printHello  # Python function to be called
    )

    # Task to send an email using the EmailOperator
    # Make sure to create an SMTP connection in Airflow UI with the conn_id 'smtp_default'
    email_task = EmailOperator(
        task_id='send_email_task',
        to='shishirsinghvaranasi@gmail.com',  # Specify the recipient email address
        subject='Airflow Task Success',  # Specify the email subject
        html_content='This is the email content',  # Specify the email content,
        conn_id='smtp_default'  # Specify the SMTP connection ID
    )

# Set the task dependencies using bitshift operator
dummy_task >> email_task
