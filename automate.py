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
import os
import requests
import git
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from datetime import datetime,timedelta

class Automation:
    def __init__(self):
        """_Python script to check for new commits using the GitHub API._
        """
        print("Hello, Thank You for viewing my code.")
        if self.datetimeUtil():
            self.CallableObject(message="Hii")
            load_dotenv()
            self.env = os.getenv
            self.log = self.setupLogger(name=self.env('LOGGER'),log_file=self.env('LOG_FILE'),level=self.env('LEVEL'))
            self.ManageCredentials()
    
    def datetimeUtil(self):
        self.localNow = datetime.utcnow() + timedelta(hours=5,minutes=30)
        self.localnow = self.localNow.strftime("%H:%M:%S.%f - %D %M,%Y")
        print(f"Current Time - {self.localnow}")
        return True
    
    def setupLogger(self,name, log_file,level):
        self.formatter = logging.Formatter('%(asctime)s %(name)-8s %(module)s %(lineno)d %(levelname)-8s %(message)s')
        handler = RotatingFileHandler(log_file, maxBytes=120000, backupCount=1, delay=False)
        handler.setFormatter(self.formatter)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.addHandler(handler)
        return self.logger
    
    def CallableObject(self,message):
        self.message = message
        print(f"Accessable - {self.message}")
        return True if self.message is not None else False
    
    def ManageCredentials(self):
        """Managed Credential"""
        # setup owner name , access_token, and headers
        self.owner = str(os.getenv('OWNER'))
        self.access_token = str(os.getenv('ACCESS_TOKEN'))
        self.headers = {'Authorization':"Token "+self.access_token}
        self.getInfo()
    
    def getInfo(self):
        """_Citation:- https://melaniesoek0120.medium.com/how-to-use-github-api-to-extract-data-with-python-bdc61106a501
        """
        self.repoInformation()
        for page in self.repos:
            if page==[]:
                print(self.repos.index(page))
                break
            
    def repoInformation(self):
        """_Loop through all pages to obtain all the repos' information
        """
        self.repos=[]
        for page_num in range(1,300):
            try:
            # to find all the repos' names from each page
                url=f"https://api.github.com/users/{self.owner}/repos?page={page_num}" 
                repo=requests.get(url,headers=self.headers).json()
                self.repos.append(repo)
            except:
                self.repos.append(None)

def main():
    clsUnit = Automation()
    return True
    
    
if __name__ == "__main__":
    main()