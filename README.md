# Git-Sevak

## Overview
**Git-Sevak** is a powerful and efficient command-line interface (CLI) tool designed to simplify GitHub repository management and system information retrieval. It enables users to perform essential Git operations directly from the terminal without relying on a graphical user interface. With Git-Sevak, users can clone repositories, create and commit files, manage GitHub issues, and fetch system details seamlessly. This tool is especially useful for developers and system administrators who frequently interact with GitHub and need a streamlined workflow for managing repositories and tracking system data.

**Disclaimer:** This project uses the GitHub API but is not affiliated with GitHub, Inc.
MAKE SURE TO CREATE AN API KEY FROM GITHUB (CLASSIC-TOKEN) AND USE IT IN THE CODE.
## Features
- Clone a GitHub repository
- Create a new folder
- Commit a file to a repository
- Commit all changes in a repository
- Retrieve GitHub repository details
- Retrieve GitHub owner details
- Create GitHub issues
- List GitHub issues
- Fetch system information

## Installation

### Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```

### Steps
1. Clone this repository:
   ```sh
   git clone <repository-url>
   cd git-sevak
   ```
You can create a virtual environment and install the required packages using pip:
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the script:
   ```sh
   git-sevak -h
   ```

## Usage

### Clone a GitHub Repository
```sh
git-sevak clone <repo_url> <destination>
```

### Create a New Folder
```sh
git-sevak create-folder <path>
```

### Commit a File
```sh
git-sevak commit-file <repo_path> <file_path> <message>
```

### Commit All Changes
```sh
git-sevak commit-all <repo_path> <message>
```

### Get Repository Details
```sh
git-sevak repo-info <owner> <repo>
```

### Get GitHub Owner Details
```sh
git-sevak owner-info <owner>
```

### Create a GitHub Issue
```sh
git-sevak create-issue <owner> <repo> <title> <body>
```

### List GitHub Issues
```sh
git-sevak list-issues <owner> <repo>
```

### Get System Information
```sh
git-sevak system-info
```

## Author
[Piyush Kumar Mondal](https://github.com/piyush182004)

## License
This project is licensed under the MIT License.

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## Issues
If you encounter any issues, please feel free to open an issue in the repository.
---

Developed with ❤️ by Piyush Kumar Mondal.

