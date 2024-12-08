python
from utils.git_api import GitHubAPI
from utils.metrics_extractor import MetricsExtractor
from utils.file_processing import ExcelWriter
from config.settings import GIT_API_TOKEN

def main():
    org_name = "your_org_name"  # Replace with the organization name
    github_api = GitHubAPI(GIT_API_TOKEN)
    metrics_extractor = MetricsExtractor(github_api)
    excel_writer = ExcelWriter()

    # Fetch repositories
    repos = github_api.get_repositories(org_name)

    # Extract metrics for each repo
    data = []
    for repo in repos:
        metrics = metrics_extractor.extract_metrics(repo)
        data.append(metrics)

    # Write metrics to Excel
    output_file = "output/git_metrics.xlsx"
    excel_writer.write_to_excel(data, output_file)
    print(f"Metrics successfully written to {output_file}")

if __name__ == "__main__":
    main()


### config/settings.py
python
GIT_API_TOKEN = "your_github_token"  # Replace with your GitHub Personal Access Token


### utils/git_api.py
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
