# vlearn_project_ci_cd_pipeline_b4
This is a simple project for CI/CD pipeline in Vlearn DevOps Batch 4
```python
"""
Create a complete CI-CD pipeline using bash, python and crontabs. The list of tasks is specified below: 

Task 1: Set Up a Simple HTML Project 
    Create a simple HTML project and push it to a GitHub repository. 
Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx
Task 3: Write a Python Script to Check for New Commits
    Create a Python script to check for new commits using the GitHub API.
Task 4: Write a Bash Script to Deploy the Code
    Create a bash script to clone the latest code and restart Nginx.
Task 5: Set Up a Cron Job to Run the Python Script
    Create a cron job to run the Python script at regular intervals.
Task 6: Test the Setup
Make a new commit to the GitHub repository and check that the changes are automatically deployed.
"""
```

###### Solution

Task 1:
    Added the simple HTML code in index.html

Task 2:
    Please refer document [kinnar_devops_b4_deployment.doc](https://docs.google.com/document/d/1o1l_LWqtSomgvfXsTkrkeFvEWWIt9HMZN48bqvCDj_c/edit?usp=sharing)

Task 3:
```bash

```
Task 4:
```bash
crontab -l
# Edit this file to introduce tasks to be run by cron.
#
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').
#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)
#
# m h  dom mon dow   command

*/2 * * * *     /home/ubuntu/automation/_cronScript.sh >> /home/ubuntu/cronjobs/log/success.log 2> /home/ubuntu/cronjobs/log/error.log >> /home/ubuntu/cronjobs/log/debug.log && sudo cp -r  /home/ubuntu/cronjobs/log/debug.log debug.txt

ubuntu@ip-172-31-36-196:~/cronjobs/log$ pwd
/home/ubuntu/cronjobs/log
ubuntu@ip-172-31-36-196:~/cronjobs/log$ ls -l
total 4
-rw-rw-r-- 1 ubuntu ubuntu 832 Feb 17 13:56 debug.log
-rw-rw-r-- 1 ubuntu ubuntu   0 Feb 17 13:56 error.log
-rw-rw-r-- 1 ubuntu ubuntu   0 Feb 17 13:50 success.log
ubuntu@ip-172-31-36-196:~/cronjobs/log$
```