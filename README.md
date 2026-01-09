# GitHubGuard

[![PyPI version](https://img.shields.io/pypi/v/GitHubGuard)](https://pypi.org/project/GitHubGuard/) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

GitHubGuard is a lightweight Python package to automatically create GitHub issues from your scripts.
It allows you to capture exceptions or messages in your Python code and turn them into issues in one or multiple repositories, with optional labels and assignees.

---

## Features

- Automatically create GitHub issues from Python scripts
- Global configuration for token and default repository
- Create issues in different repositories dynamically
- Add custom title, labels, and assignees
- Easy to import and use across multiple scripts
- Fully compatible with Python 3.8+
- 
---

## Installation

Install via pip:
```bash
pip install GitHubGuard
```

Or if using your local development version:
```bash
pip install -e .
```

---

## Usage
```python3
from GitHubGuard import config, create_issue

# Configure once
config(token="your-github-token", default_repo="username/MyRepo")

try:
    1 / 0
except Exception as e:
    create_issue(
        str(e),
        title="Critical error in script",
        labels=["bug", "urgent"],
        assignees=["username1", "username2"]
    )
```
- `token` – Your GitHub personal access token
- `default_repo` – Default repository in owner/repo format
- `title` – Optional custom title (default: first 50 characters of message)
- `labels` – List of labels to assign to the issue
- `assignees` – List of GitHub usernames to assign the issue

You can also create issues in different repositories without changing the global configuration:

```python3
create_issue(
    "Another error occurred",
    repo="username/OtherRepo",
    labels=["enhancement"],
)
```

---

## License
This project is licensed under the MIT License.

---

## Contributing
Feel free to fork, modify, and submit pull requests. Bug reports and suggestions are welcome!

---