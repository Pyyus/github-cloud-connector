import requests # type: ignore
from app.config import GITHUB_TOKEN, GITHUB_BASE_URL

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_repos(username: str):
    response = requests.get(f"{GITHUB_BASE_URL}/users/{username}/repos", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def list_issues(owner: str, repo: str):
    response = requests.get(f"{GITHUB_BASE_URL}/repos/{owner}/{repo}/issues", headers=HEADERS)
    response.raise_for_status()
    return response.json()

def create_issue(owner: str, repo: str, title: str, body: str):
    payload = {"title": title, "body": body}
    response = requests.post(f"{GITHUB_BASE_URL}/repos/{owner}/{repo}/issues", json=payload, headers=HEADERS)
    response.raise_for_status()
    return response.json()