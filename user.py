from github import Github

github_url = "https://api.github.com/users/{username}"

class User:
    def __init__(self, username):
        self.url = github_url.format(username=username)
        self.github = Github()

        self.user = self.github.get_user(username)
