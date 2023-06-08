# Peer Review
# Kushagra's review
Task 1
In this task, he successfully created a DAG named dag1 that runs on a daily schedule. 
The DAG contains three operations: create_table, insert_data, and select_data. 
These operations effectively handle the creation of a table named users if it doesn't already exist, inserting data into the table, and selecting 
data from the created table.

Task 2
For this task, he created a DAG called dummy_dag that is also scheduled daily.
Within this DAG, he implemented two operations: dummy_task and send_mail. 
The dummy_task has been appropriately designed to always pass, indicating its successful execution. 
Additionally, the send_mail operation has been included to notify the developer of the task's successful completion

Task 3
The slack_alert_dag he created is scheduled daily and consists of three operations: dummy_task, success_failure_task, and slack_alert_task. 
The dummy_task has been implemented to consistently pass, while the success_failure_task serves as a simulated task that can either pass or fail. 
Finally, the slack_alert_task has been incorporated to send a message to Slack, providing information about the outcome of the success_failure_task.


# Ayush's review
Task 1
In this task, he successfully created a DAG named "table_dag" that creates a "users" table in a Postgres database, inserts data into the table, and selects 
and displays the data. 
The DAG consists of three tasks: create_table, insert_data, and select_data, with dependencies defined in the order of execution.
1. create_table task, which uses PostgresOperator to create a "users" table in the Postgres database if it doesn't exist.
2. insert_data task, utilizing BashOperator, executes a bash command to insert data into the "users" table.
3. select_data task, also using BashOperator, runs a bash command to select and display all data from the "users" table.

Task 2
In this task, he successfully created a DAG named "email_dag" that includes two tasks
1. The dummy_task is an EmptyOperator task that does not perform any specific operation. It serves as a placeholder or a trigger point in the DAG.
2. The email_task is an EmailOperator task that sends an email. It is configured with the recipient email address, subject, HTML content, and a connection ID named "smtp_default" to handle the email configuration.

The dag uses default arguments that specify the owner, number of retries, and retry delay.
The catchup flag is set to False, preventing backfilling of previous time periods. 
The dummy_task is set as the preceding task of the email_task, defining their dependency in the DAG.

Task 3
In this task, he successfully created a DAG named "slack_dag" that includes three tasks
1. The dummy_task is a PythonOperator that executes the dummyConditionalTask function.
2. The success_task is a SlackWebhookOperator that sends a success message to a Slack channel using the provided webhook connection. It is set to trigger only when all preceding tasks have succeeded.
3. The fail_task is another SlackWebhookOperator that sends a failure message to a Slack channel when any preceding task has failed.

The tasks are scheduled to start on April 17, 2023, with a daily interval. The catchup parameter is set to False, preventing backfilling of previous time periods. 
The dependency between the tasks is set up such that the dummy_task is followed by both the success_task and fail_task.



