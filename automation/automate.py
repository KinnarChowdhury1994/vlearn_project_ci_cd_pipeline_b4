# import requests
# import subprocess

# def check_for_new_commits():
#     # Replace 'your-username' and 'your-repo' with your GitHub username and repository name
#     repo_url = "https://api.github.com/repos/KinnarChowdhury1994/your-repo/commits%22
    
#     response = requests.get(repo_url)
#     commits = response.json()

#     latest_commit_hash = commits[0]['sha']

#     return latest_commit_hash

# if __name__ == "__main__":
#     latest_commit_hash = check_for_new_commits()
#     print(f"Latest Commit Hash: {latest_commit_hash}")


from datetime import datetime,timedelta
import logging
from logging.handlers import RotatingFileHandler
import os
from dotenv import load_dotenv
from constants import GITHUB_API,REPOSITORY,UTF8
import http.client
import json
import subprocess

class Automation:
    def __init__(self):
        """_Python script to check for new commits using the GitHub API._
        """
        print("Hello, Thank You for viewing my code.")
        try:
            if self.datetimeUtil():
                self.ManageCredentials()
                gitResp = self.retrieve_latest_commit_date_for_github_repository(in_repository_name=str(REPOSITORY))
                self.log.warning(gitResp)
                
                if gitResp:
                    self.log.warning('Processing for Deployment')
                    subprocess.Popen('echo "Testing in Server Console"', shell=True)
                    subprocess.Popen('pwd', shell=True)
                    subprocess.Popen('ls -la', shell=True)
                    subprocess.Popen('cd /home/kinnar/deployment/automation"', shell=True)
                    subprocess.Popen('pwd', shell=True)
                    subprocess.Popen('ls -l', shell=True)
                    subprocess.Popen('sh _deploy.sh', shell=True)
                    self.log.warning('Deployment Script Triggered Successfully')
                    
                else:
                    self.log.warning('No Deployment')
                
            else:
                raise Exception('Error Occured')
        except Exception as e:
            print(e)
        finally:
            print('Execution Completed')
    
    def datetimeUtil(self):
        localNow = datetime.utcnow() + timedelta(hours=5,minutes=30)
        localnow = localNow.strftime("%H:%M:%S.%f - %D %M,%Y")
        load_dotenv()
        self.env = os.getenv
        self.log = self.setupLogger(name=self.env('LOGGER'),log_file=self.env('LOG_FILE'),level=self.env('LEVEL'))
        self.log.info(f"[Inside - datetimeUtil function] Current Time - {localnow}")
        return True
    
    def setupLogger(self,name, log_file,level):
        """Setting Up Logger"""
        formatter = logging.Formatter('%(asctime)s %(name)-8s %(module)s %(lineno)d %(levelname)-8s %(message)s')
        handler = RotatingFileHandler(log_file, maxBytes=120000, backupCount=1, delay=False)
        handler.setFormatter(formatter)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger
    
    def ManageCredentials(self):
        """Managed Credential"""
        # setup owner name , access_token, and headers
        self.owner = str(os.getenv('OWNER'))
        self.access_token = str(os.getenv('ACCESS_TOKEN'))
        self.headers = {'Authorization':"Bearer " + self.access_token}

    def retrieve_latest_commit_date_for_github_repository(self, in_repository_name):
        """Retrieves the date of the last commit for the master branch of the user's GitHub repository.

        :param in_username: Name of user which repository to get last commit for.
        :param in_repository_name Name of user's repository for which to get last commit for.
        :return: String containing date of last commit, or None if GitHub request failed.
        :Link: https://www.ivankrizsan.se/2017/03/19/interacting-with-github-using-python/
        """
        https_conn = http.client.HTTPSConnection(f'{GITHUB_API}')
        repo_last_commit_date = None
        http_request_headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": self.owner}
        latest_push = False
        try:
            # Request only the one last commit for the supplied user's repository with supplied name.
            self.log.info('Inside retrieve_latest_commit_date_for_github_repository function')
            github_request_path = f"/repos/{str(self.owner)}/{in_repository_name}/commits?page=1&per_page=1"
            # github_request_path = f"/repos/{str(self.owner)}/{in_repository_name}/commits"
            self.log.warning(f'github_request_path -> {github_request_path}')
            
            https_conn.request(url=github_request_path,method='GET',headers=http_request_headers)
            git_api_resp = https_conn.getresponse()
            resp_data = git_api_resp.read().decode(f'{UTF8}')
            self.log.warning(f'Status :: {git_api_resp.status}')    # | Github API Response ->\n{resp_data}')
            
            if git_api_resp.status == 200:
                # Response was successful, now read and parse the JSON data.
                api_resp_text = resp_data
                # self.log.warning(f'api_resp_text\n{api_resp_text}')
                
                api_resp_object = json.loads(api_resp_text)
                # self.log.warning(f'api_resp_object\n{api_resp_object}')
                
                interval = 0
                total_len = len(api_resp_object)
                self.log.info(f'Total Commits :: {total_len}')
                
                curr_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
                curr_time = datetime.strptime(curr_time,"%Y-%m-%dT%H:%M:%SZ")
                self.log.warning(f'Current Time -> {curr_time}')
                
                # for i in range(len(api_resp_object)):
                #     last_commit_ref = api_resp_object[i]['sha']
                #     last_commit_msg = api_resp_object[i]['commit']['message']
                #     committed_by = api_resp_object[i]['commit']['committer']['name']
                #     repo_last_commit_date = api_resp_object[i]['commit']['author']['date']
                #     # self.log.warning(f'repository_last_commit_date -> {repo_last_commit_date} :: Datatype = {type(repo_last_commit_date)}')
                #     repo_last_commit_date = datetime.strptime(repo_last_commit_date, "%Y-%m-%dT%H:%M:%SZ")
                #     # self.log.warning(f'[CONVERT] repository_last_commit_date -> {repo_last_commit_date} :: Datatype = {type(repo_last_commit_date)}')
                last_commit_ref = api_resp_object[0]['sha']
                last_commit_msg = api_resp_object[0]['commit']['message']
                committed_by = api_resp_object[0]['commit']['committer']['name']
                repo_last_commit_date = api_resp_object[0]['commit']['author']['date']
                # self.log.warning(f'repository_last_commit_date -> {repo_last_commit_date} :: Datatype = {type(repo_last_commit_date)}')
                repo_last_commit_date = datetime.strptime(repo_last_commit_date, "%Y-%m-%dT%H:%M:%SZ")
                # self.log.warning(f'[CONVERT] repository_last_commit_date -> {repo_last_commit_date} :: Datatype = {type(repo_last_commit_date)}')
                
                interval = (curr_time - repo_last_commit_date)
                seconds = interval.total_seconds()
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                seconds = seconds % 60
                
                self.log.info(f'Interval of Current Time & Last Commit Time :: {interval} Timedelta [ H :: {hours} | M :: {minutes} | S :: {seconds}]')
                
                if ((minutes > 0.0 and minutes < 5.0) and (hours == 0.0)):
                    self.log.info('New Commit Found')
                    latest_push = True
                else:
                    self.log.info('No New Commit Found')
                self.log.warning(f'Reference {last_commit_ref} [{last_commit_ref[0:7]}] | Last Commit Msg -> {last_commit_msg} ::|:: BY - {committed_by} ON - {repo_last_commit_date}')                    
            else:
                message = f"ERROR: Request to GitHub failed with status {git_api_resp.status} and the reason was {git_api_resp.reason}"
                self.log.error(f'Message -> {message}')
        except Exception as e:
            self.log.exception(e)
            latest_push = False
        finally:
            https_conn.close()
            self.log.warning("HTTP Connection Closed Successfully")
            return latest_push

def main():
    clsUnit = Automation()
    try:
        print("OK")
    except Exception as e:
        clsUnit.log.exception(e)
    finally:
        return 200,"SUCCESS"
    
    
if __name__ == "__main__":
    main()