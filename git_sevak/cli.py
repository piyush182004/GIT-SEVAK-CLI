import argparse
from git_sevak.github_api import get_repo_details, get_owner_details, create_issue, list_issues
from git_sevak.git_operations import clone_repo, create_folder, commit_file, commit_all_changes
from git_sevak.system_info import get_system_info

def main():
    parser = argparse.ArgumentParser(description="Git-Sevak: CLI for GitHub & System Info ....Author Piyush Mondal")

    subparsers = parser.add_subparsers(dest="command")

    # Clone Repo
    clone_parser = subparsers.add_parser("clone", help="Clone a GitHub repository")
    clone_parser.add_argument("repo_url", help="GitHub repository URL")
    clone_parser.add_argument("destination", help="Destination folder")

    # Create Folder
    folder_parser = subparsers.add_parser("create-folder", help="Create a new folder")
    folder_parser.add_argument("path", help="Path of the new folder")

    # Commit a File
    commit_file_parser = subparsers.add_parser("commit-file", help="Commit a new file to a repo")
    commit_file_parser.add_argument("repo_path", help="Path to the Git repository")
    commit_file_parser.add_argument("file_path", help="File to commit")
    commit_file_parser.add_argument("message", help="Commit message")

    # Commit All Changes
    commit_all_parser = subparsers.add_parser("commit-all", help="Commit all changes in a repo")
    commit_all_parser.add_argument("repo_path", help="Path to the Git repository")
    commit_all_parser.add_argument("message", help="Commit message")

    # Repository Details
    repo_parser = subparsers.add_parser("repo-info", help="Get GitHub repository details")
    repo_parser.add_argument("owner", help="Repository owner")
    repo_parser.add_argument("repo", help="Repository name")

    # Owner Details
    owner_parser = subparsers.add_parser("owner-info", help="Get GitHub owner details")
    owner_parser.add_argument("owner", help="GitHub owner username")

    # Create Issue
    issue_parser = subparsers.add_parser("create-issue", help="Create a GitHub issue")
    issue_parser.add_argument("owner", help="Repository owner")
    issue_parser.add_argument("repo", help="Repository name")
    issue_parser.add_argument("title", help="Issue title")
    issue_parser.add_argument("body", help="Issue description")

    # List Issues
    issues_parser = subparsers.add_parser("list-issues", help="List GitHub issues")
    issues_parser.add_argument("owner", help="Repository owner")
    issues_parser.add_argument("repo", help="Repository name")

    # System Info
    subparsers.add_parser("system-info", help="Get system information")

    args = parser.parse_args()

    if args.command == "clone":
        print(clone_repo(args.repo_url, args.destination))
    elif args.command == "create-folder":
        print(create_folder(args.path))
    elif args.command == "commit-file":
        print(commit_file(args.repo_path, args.file_path, args.message))
    elif args.command == "commit-all":
        print(commit_all_changes(args.repo_path, args.message))
    elif args.command == "repo-info":
        print(get_repo_details(args.owner, args.repo))
    elif args.command == "owner-info":
        print(get_owner_details(args.owner))
    elif args.command == "create-issue":
        print(create_issue(args.owner, args.repo, args.title, args.body))
    elif args.command == "list-issues":
        print(list_issues(args.owner, args.repo))
    elif args.command == "system-info":
        print(get_system_info())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
