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
The slack.py DAG sends a message to a specified Slack channel using a Slack webhook. 
The DAG is scheduled to run daily, and consists of the following tasks:

* dummy_task: a task that raises an exception randomly
* success_task: sends a success message to a Slack channel if all tasks succeed
* fail_task: sends a failure message to a Slack channel if any task fails
