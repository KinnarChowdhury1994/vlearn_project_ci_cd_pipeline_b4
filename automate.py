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

class Automation:
    def __init__(self):
        """_Python script to check for new commits using the GitHub API._
        """
        print("Hello, Thank You for viewing my code.")
        try:
            if self.datetimeUtil():
                self.ManageCredentials()
                self.retrieve_latest_commit_date_for_github_repository(in_username=str(self.owner),in_repository_name=str(REPOSITORY))
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

    def retrieve_latest_commit_date_for_github_repository(self,in_username, in_repository_name):
        """Retrieves the date of the last commit for the master branch of the user's GitHub repository.

        :param in_username: Name of user which repository to get last commit for.
        :param in_repository_name Name of user's repository for which to get last commit for.
        :return: String containing date of last commit, or None if GitHub request failed.
        """
        https_conn = http.client.HTTPSConnection(f'{GITHUB_API}')
        repository_last_commit_date = None
        http_request_headers = {"Accept": "application/vnd.github.v3+json", "User-Agent": self.owner}

        try:
            # Request only the one last commit for the supplied user's repository with supplied name.
            self.log.info('Inside retrieve_latest_commit_date_for_github_repository function')
            github_request_path = "/repos/" + in_username + "/" + in_repository_name + "/commits?page=1&per_page=1"
            self.log.warning(f'github_request_path -> {github_request_path}')
            
            https_conn.request(url=github_request_path,method='GET',headers=http_request_headers)
            git_api_resp = https_conn.getresponse()
            resp_data = git_api_resp.read().decode(f'{UTF8}')
            self.log.warning(f'Status :: {git_api_resp.status} | Github API Response ->\n{resp_data}')
            
            if git_api_resp.status == 200:
                # Response was successful, now read and parse the JSON data.
                api_resp_text = resp_data
                # self.log.warning(f'api_resp_text\n{api_resp_text}')
                
                api_resp_object = json.loads(api_resp_text)
                # self.log.warning(f'api_resp_object\n{api_resp_object}')
                
                last_commit_ref = api_resp_object[0]['sha']
                last_commit_msg = api_resp_object[0]['commit']['message']
                committed_by = api_resp_object[0]['commit']['committer']['name']
                repo_last_commit_date = api_resp_object[0]['commit']['author']['date']
                self.log.warning(f'repository_last_commit_date -> {repository_last_commit_date}')
                self.log.warning(f'Reference {last_commit_ref} [{last_commit_ref[0:7]}] | Last Commit Message -> {last_commit_msg} | By {committed_by} on {repo_last_commit_date}')
            else:
                message = f"ERROR: Request to GitHub failed with status {git_api_resp.status} and the reason was {git_api_resp.reason}"
                self.log.error(f'Message -> {message}')
        finally:
            https_conn.close()

def main():
    clsUnit = Automation()
    try:
        print("OK")
    except Exception as e:
        clsUnit.log.exception(e)
    finally:
        return 200
    
    
if __name__ == "__main__":
    main()