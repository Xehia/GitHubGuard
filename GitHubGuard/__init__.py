from .core import GitHubGuard

guard = GitHubGuard()

def config(token=None, default_repo=None):
    guard.set_config(token=token, default_repo=default_repo)

def create_issue(message, repo=None, title=None, labels=None, assignees=None):
    return guard.create_issue(
        message=message,
        repo=repo,
        title=title,
        labels=labels,
        assignees=assignees
    )
