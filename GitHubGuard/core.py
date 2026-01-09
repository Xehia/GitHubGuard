import requests

class GitHubGuard:
    """
    Main class for creating GitHub issues automatically.
    """

    def __init__(self):
        self.token = None
        self.default_repo = None  # format: "owner/repo"

    def set_config(self, token=None, default_repo=None):
        """
        Set GitHub token and default repository.

        :param token: GitHub personal access token
        :param default_repo: default repository in "owner/repo" format
        """
        if token:
            self.token = token
        if default_repo:
            self.default_repo = default_repo

    def create_issue(self, message, repo=None, title=None, labels=None, assignees=None):
        """
        Create a GitHub issue.

        :param message: main body of the issue
        :param repo: target repository (format "owner/repo")
        :param title: title of the issue (default: first 50 characters of message)
        :param labels: list of labels to assign to the issue
        :param assignees: list of GitHub usernames to assign the issue to
        :return: JSON response from GitHub API
        """
        if not self.token:
            raise ValueError("GitHub token is not set. Use set_config() first.")
        repo_to_use = repo or self.default_repo
        if not repo_to_use:
            raise ValueError("No repository specified.")

        url = f"https://api.github.com/repos/{repo_to_use}/issues"
        headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github+json"
        }
        data = {
            "title": title[:50] if title else message[:50],
            "body": message
        }
        if labels:
            data["labels"] = labels
        if assignees:
            data["assignees"] = assignees

        response = requests.post(url, json=data, headers=headers)
        if response.status_code != 201:
            raise Exception(f"Failed to create issue: {response.status_code} {response.text}")
        return response.json()
