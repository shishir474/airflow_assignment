# Table DAG - table.py
The table.py DAG creates a PostgreSQL table named users and inserts some sample data into it. 
The DAG is scheduled to run daily, and consists of the following tasks:

* create_table: creates the users table if it doesn't exist already
* insert_data: inserts sample data into the users table
* select_data: selects all data from the users table

# Email DAG - email.py
The email.py DAG sends an email to a specified recipient using the default SMTP connection. 
The DAG is scheduled to run daily, and consists of the following tasks:

* dummy_task: a dummy task that does nothing
* email_task: sends an email with a subject and some content to a specified recipient

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
