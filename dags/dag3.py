from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator

# Define a Python function to be called by the PythonOperator task
def dummyConditionalTask():
    import random
    x=random.randint(1,100)
    if x>50:
        raise Exception()

# Create a DAG with a specified DAG ID, start date, schedule interval, and catch-up option
with DAG(dag_id='slack_dag',start_date=datetime(2023,4,17),schedule_interval='@daily',catchup=False) as dag:
    # Task to call the dummyConditionalTask function using PythonOperator
    dummy_task=PythonOperator(
        task_id='dummy_task',
        python_callable=dummyConditionalTask  # Python function to be called
    )

    # Task to send a success message to Slack using the SlackWebhookOperator
    success_task=SlackWebhookOperator(
        task_id='success_task',
        http_conn_id='slack',  # Specify the Slack connection ID
        message=':smile: Task Successfully Run',  # Specify the success message
        trigger_rule='all_success'  # Specify the trigger rule for success
    )

    # Task to send a failure message to Slack using the SlackWebhookOperator
    fail_task=SlackWebhookOperator(
        task_id='fail_task',
        http_conn_id='slack',  # Specify the Slack connection ID
        message=':red_circle: Task Failed',  # Specify the failure message
        trigger_rule='all_failed'  # Specify the trigger rule for failure
    )

# Set the task dependencies using bitshift operator
dummy_task >> [success_task,fail_task]
