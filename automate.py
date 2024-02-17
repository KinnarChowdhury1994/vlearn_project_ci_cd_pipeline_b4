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
import requests
import git
class Automation:
    def __init__(self):
        """_Python script to check for new commits using the GitHub API._
        """
        import requests
        self.CallableObject()
        
    def CallableObject(self,message):
        self.message = message
        return print(f"Accessable - {self.message}")