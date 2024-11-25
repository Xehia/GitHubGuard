import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from a .env file
BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

# Retrieve GitHub token from environment variables
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GitHub token not found. Ensure 'GITHUB_TOKEN' is set in the .env file.")

# GitHub repository details
username = "Xehia"  # GitHub username
repository_name = "GitHubGuard"  # Repository name

def create_issue(error_message):
    """
    Creates a GitHub issue in the specified repository.
    
    Args:
        error_message (str): The message to include in the issue body.
    """
    title = "Error Detected: Automated Issue Report"  # Issue title
    body = f"An error occurred in the script:\n\n```\n{error_message}\n```"  # Issue body with error details
    labels = ["bug"]  # Label(s) for the issue
    assignees = ["Xehia"]  # Assign the issue to the specified user(s)

    # Set up the request headers and data payload
    headers = {
        "Authorization": f"token {token}",  # Add the authorization token
        "Accept": "application/vnd.github.v3+json"  # Specify GitHub API version
    }
    data = {
        "title": title,
        "body": body,
        "labels": labels,
        "assignees": assignees
    }

    # GitHub API endpoint for creating issues
    url = f"https://api.github.com/repos/{username}/{repository_name}/issues"

    # Send a POST request to create the issue
    response = requests.post(url, json=data, headers=headers)

    # Check the response for success or failure
    if response.status_code == 201:
        print(f"Issue successfully created: {response.json().get('html_url')}")
    else:
        print(f"Failed to create issue. Status code: {response.status_code}")
        print(f"Response: {response.text}")

try:
    # Example code to trigger an exception (division by zero)
    an_error = 1 / 0
except Exception as e:
    print(f"An error occurred: {e}")
    create_issue(str(e))  # Pass the error message to the create_issue function
