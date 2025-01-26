import os
import subprocess

def clone_repo(repo_url, destination):
    result = subprocess.run(["git", "clone", repo_url, destination], capture_output=True, text=True)
    return result.stdout

def create_folder(path):
    os.makedirs(path, exist_ok=True)
    return f"Folder created at {path}"

def commit_file(repo_path, file_path, message):
    subprocess.run(["git", "add", file_path], cwd=repo_path)
    result = subprocess.run(["git", "commit", "-m", message], cwd=repo_path, capture_output=True, text=True)
    return result.stdout

def commit_all_changes(repo_path, message):
    subprocess.run(["git", "add", "."], cwd=repo_path)
    result = subprocess.run(["git", "commit", "-m", message], cwd=repo_path, capture_output=True, text=True)
    return result.stdout
