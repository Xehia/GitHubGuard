from .core import GitHubGuard

# Global instance for quick import
guard = GitHubGuard()

def config(token=None, default_repo=None):
    """
    Configure GitHub token and default repository.
    """
    guard.set_config(token=token, default_repo=default_repo)

def create_issue(message, repo=None, title=None, labels=None, assignees=None):
    """
    Create a GitHub issue using the global instance.
    """
    return guard.create_issue(
        message=message,
        repo=repo,
        title=title,
        labels=labels,
        assignees=assignees
    )
