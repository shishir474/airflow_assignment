from airflow import DAG
from datetime import datetime
from airflow.operators.email import EmailOperator
from airflow.operators.empty import EmptyOperator

with DAG('email_dag', start_date=datetime(2022,1,1), schedule_interval='@once', catchup=False):
  # define an EmptyOperator task
  dummy_task = EmptyOperator(
    task_id = 'default_task',
  )

  # create smtp connection on airflow UI. 
  # define an EmailOperator task
  email_task = EmailOperator(
    task_id='send_email_task',
    to='shishirsinghvaranasi@gmail.com',  # Specify the recipient email address
    subject='Airflow Task Success',  # Specify the email subject
    html_content='Sending some dummy content',  # Specify the email content,
    conn_id='smtp_default'
  )

  # set the dependency between the two tasks
  dummy_task >> email_task

