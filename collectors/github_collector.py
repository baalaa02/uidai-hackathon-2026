import requests
import base64

def get_default_branch(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json().get("default_branch", "main")

def get_repo_tree(owner, repo):
    branch = get_default_branch(owner, repo)
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["tree"]

def fetch_file(owner, repo, path):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url)
    response.raise_for_status()
    content = response.json()
    if content.get("encoding") == "base64":
        return base64.b64decode(content["content"]).decode("utf-8", errors="ignore")
    return ""
