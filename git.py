import subprocess
import requests

# GitHub API and Authentication
TOKEN = "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"  # Replace with your GitHub token
REPO_OWNER = "gogo-byte"  # Replace with the repository owner's username
REPO_NAME = "GlitchHackathon"  # Replace with your repository name
BRANCH_NAME = "feature/testbranch"  # The branch you're working on
BASE_BRANCH = "main"  # The base branch for the pull request

# Step 1: Git Add, Commit, and Push
def git_add_commit_push():
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)
        commit_message = input("Enter commit message: ")
        # Commit changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        # Push changes to the remote repository
        subprocess.run(["git", "push", "origin", BRANCH_NAME], check=True)
        print(f"Pushed changes to the branch: {BRANCH_NAME}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operations: {e}")
        return False
    return True

# Step 2: Create a Pull Request
def create_pull_request():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    pr_data = {
        "title": f"PR from {BRANCH_NAME}",
        "head": BRANCH_NAME,  # The branch you're working on
        "base": BASE_BRANCH,  # The base branch you're merging into
        "body": "Automated pull request created via Python script."
    }
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        response = requests.post(url, json=pr_data, headers=headers)
        response.raise_for_status()  # Will raise an exception for HTTP errors
        print(f"Pull request created successfully: {response.json()['html_url']}")
    except requests.exceptions.RequestException as e:
        print(f"Error creating pull request: {e}")

# Main function
def main():
    if git_add_commit_push():
        create_pull_request()

if __name__ == "__main__":
    main()
