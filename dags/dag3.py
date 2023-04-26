from airflow import DAG
from datetime import datetime

from airflow.operators.python import PythonOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator

def dummyConditionalTask():
    import random
    x=random.randint(1,100)
    if x>50:
        raise Exception()

with DAG(dag_id='slack_dag',start_date=datetime(2023,4,17),schedule_interval='@daily',catchup=False) as dag:
    dummy_task=PythonOperator(
        task_id='dummy_task',
        python_callable=dummyConditionalTask
    )

    success_task=SlackWebhookOperator(
        task_id='success_task',
        http_conn_id='slack',
        message=':smile: Task Successfully Run',
        trigger_rule='all_success'
    )

    fail_task=SlackWebhookOperator(
        task_id='fail_task',
        http_conn_id='slack',
        message=':red_circle: Task Failed',
        trigger_rule='all_failed'
    )

    dummy_task >> [success_task,fail_task]


# https://hooks.slack.com/services/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