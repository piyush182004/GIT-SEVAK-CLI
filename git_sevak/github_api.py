import requests

GITHUB_API_KEY = "get_api_key"
HEADERS = {"Authorization": f"token {GITHUB_API_KEY}"}

def get_repo_details(owner, repo):
    # Fetching the repository details
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url, headers=HEADERS)
    repo_data = response.json()

    # Extracting relevant repo details like stars, forks, and issues
    repo_details = {
        "stars": repo_data.get("stargazers_count", "Not available"),
        "forks": repo_data.get("forks_count", "Not available"),
        "open_issues": repo_data.get("open_issues_count", "Not available")
    }
    return repo_details

def get_owner_details(owner):
    # Fetching user details
    url = f"https://api.github.com/users/{owner}"
    response = requests.get(url, headers=HEADERS)
    user_data = response.json()

    # Extracting user details like number of repositories, followers, join date, etc.
    owner_details = {
        "name": user_data.get("name", "Not available"),
        "login": user_data.get("login", "Not available"),
        "followers": user_data.get("followers", "Not available"),
        "repos_count": user_data.get("public_repos", "Not available"),
        "joined": user_data.get("created_at", "Not available"),
        "stars": user_data.get("public_gists", "Not available")  # public gists as a substitute for star count
    }
    return owner_details

def create_issue(owner, repo, title, body):
    # Creating a new issue in a repo
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    data = {"title": title, "body": body}
    response = requests.post(url, json=data, headers=HEADERS)
    return response.json()

def list_issues(owner, repo):
    # Listing issues for a repo
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    response = requests.get(url, headers=HEADERS)
    return response.json()
