# Table DAG - table.py
The table.py DAG creates a PostgreSQL table named users and inserts some sample data into it. 
The DAG is scheduled to run daily, and consists of the following tasks:

* create_table: creates the users table if it doesn't exist already
* insert_data: inserts sample data into the users table
* select_data: selects all data from the users table

<img width="1440" alt="Screenshot 2023-06-08 at 5 08 10 PM" src="https://github.com/shishir474/airflow_assignment/assets/57223710/1d4b166a-9200-49f8-a8d1-c9e93e3a1933">
<img width="1440" alt="Screenshot 2023-06-08 at 5 09 09 PM" src="https://github.com/shishir474/airflow_assignment/assets/57223710/26ca26e0-8bb0-45ed-9bd8-5d1754210a58">



# Email DAG - email.py
The email.py DAG sends an email to a specified recipient using the default SMTP connection. 
The DAG is scheduled to run daily, and consists of the following tasks:

* dummy_task: a dummy task that does nothing
* email_task: sends an email with a subject and some content to a specified recipient

<img width="1440" alt="Screenshot 2023-06-08 at 5 11 39 PM" src="https://github.com/shishir474/airflow_assignment/assets/57223710/b3c95ca1-32f9-4225-ad09-d6f6d02b8713">


# Slack DAG - slack.py
Create a slack web hook connection in airflow
1. Here we need to create a slack webhook connection in the airflow UI
2. Navigate to the Admin menu and select Connections.
3. Create a new connection. Enter the connection_id, connection_type as 'http' and host. 

Now once we have a connection setup succesfully, we can use that connection to send a message to the slack channel
The slack.py DAG sends a message to a specified Slack channel using a Slack webhook. 
The DAG is scheduled to run daily, and consists of the following tasks:

* dummy_task: a task that raises an exception randomly
* success_task: sends a success message to a Slack channel if all tasks succeed
* fail_task: sends a failure message to a Slack channel if any task fails

The success_task and fail_task is created using slackwebhookoperator. Here we need to specify the connection_id and the message that we want to send in slack.
The dummy_task uses python operator to call a python function, which will raise an exception randomly. So if the dummy_task succeeds, then the success_task will be executed and if it fails then fail_task will be executed.

<img width="1424" alt="234229306-18e08297-cf0f-4cf9-8601-a727bc13a5fb" src="https://github.com/shishir474/airflow_assignment/assets/57223710/c7a383c3-9b88-4539-8b85-f6ac5be311d3">
<img width="1421" alt="234229024-efc7fbd8-b88d-4ab5-8f1b-8dced8377a72 (1)" src="https://github.com/shishir474/airflow_assignment/assets/57223710/b5e5d0bb-daf7-4f3c-a7c4-bd059427b9bd">
<img width="1440" alt="Screenshot 2023-06-08 at 4 22 31 PM" src="https://github.com/shishir474/airflow_assignment/assets/57223710/cbae06af-6406-417a-a90d-9b443a6bf8f2">

# My Connections for all the given tasks
<img width="1440" alt="task3" src="https://github.com/shishir474/airflow_assignment/assets/57223710/9ab9076b-1a68-49d1-bb6a-377154e89706">

