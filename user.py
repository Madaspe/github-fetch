from github import Github

from settings import TOKEN

github_url = "https://api.github.com/users/{username}"

class User:
    def __init__(self, username):
        self.url = github_url.format(username=username)
        self.github = Github(TOKEN)
        self.username = username
        self.user = self.github.get_user(username)

    def get_info(self):
        name = self.user.name
        repos = self.user.public_repos
        followers = self.user.followers
        following = self.user.following

        return f"Name:{name}\nRepos:{repos}\nFollowers:{followers}\nFollowing:{following}"

