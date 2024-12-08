python
import requests

class GitHubAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.github.com"

    def _headers(self):
        return {"Authorization": f"Bearer {self.token}"}

    def get_repositories(self, org_name):
        url = f"{self.base_url}/orgs/{org_name}/repos"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def get_commits(self, repo_full_name, since=None):
        url = f"{self.base_url}/repos/{repo_full_name}/commits"
        params = {"since": since} if since else {}
        response = requests.get(url, headers=self._headers(), params=params)
        response.raise_for_status()
        return response.json()

    def get_contributors(self, repo_full_name):
        url = f"{self.base_url}/repos/{repo_full_name}/contributors"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()

    def get_repo_details(self, repo_full_name):
        url = f"{self.base_url}/repos/{repo_full_name}"
        response = requests.get(url, headers=self._headers())
        response.raise_for_status()
        return response.json()
