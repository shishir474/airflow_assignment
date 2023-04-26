from airflow import DAG
from datetime import datetime
from airflow.operators.email import EmailOperator
from airflow.operators.python import PythonOperator

def printHello():
    print('hello world')


with DAG('dag2', start_date=datetime(2022,1,1), schedule_interval='@daily', catchup=False):
  dummy_task = PythonOperator(
    task_id = 'dummy_task',
    python_callable=printHello
  )

# create smtp connection on airflow UI. 
  email_task = EmailOperator(
    task_id='send_email_task',
    to='shishirsinghvaranasi@gmail.com',  # Specify the recipient email address
    subject='Airflow Task Success',  # Specify the email subject
    html_content='This is the email content',  # Specify the email content,
    conn_id='smtp_default'
)

dummy_task >> email_task


# humxitezrqdoyaxc