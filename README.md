# GitHubGuard

![logo](https://s7.gifyu.com/images/SGnLw.gif)

**GitHubGuard** is a Python script that automatically creates GitHub issues when an error is detected during script execution.  
It simplifies error tracking and ensures that problems are logged in your repository for review and resolution.

---

## Features

- **Automated Issue Creation**  
  Detects errors in your Python script and creates detailed GitHub issues with error messages.

- **Customizable Issue Details**  
  Predefines issue titles, labels, and assigns issues to specific users.

- **Secure Token Handling**  
  Utilizes environment variables to securely manage your GitHub API token.

- **Error Logging**  
  Logs the error directly into your GitHub repository for easy tracking.

---

## Requirements

- Python 3.7 or higher  
- A GitHub repository where issues can be created  
- A GitHub personal access token with `repo` permissions  

---

## Installation

1. Clone the repository:
   ```
   bash git clone https://github.com/yourusername/GitHubGuard.git
   ```
2. Navigate to the project directory:
   ```
   cd GitHubGuard
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root and add your GitHub token:
   ```
   GITHUB_TOKEN=your_personal_access_token
   ```
5. Update the script with your GitHub username and repository name:
   ```
   username = "YourGitHubUsername"
   repository_name = "YourRepositoryName"
   ```

---

## Usage

1. Run the script:
   ```
   python script.py
   ```
2. When an error occurs, the script will:
  - Print the error details to the console.
  - Automatically create an issue in the specified GitHub repository with the error details.

---

## Disclaimer
This script is a utility tool and should only be used with proper authorization for creating issues in your repository. Misuse could result in unintended changes to your repository.

---

## Contributing
Contributions are welcome! If you’d like to add features or report a bug, feel free to open a pull request or issue.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
