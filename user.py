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
        info = {}

        info["Name"] = self.user.name
        info["Repos"] = self.user.public_repos
        info["Followers"] = self.user.followers
        info["Following"] = self.user.following
        info["Bio"] = self.user.bio
        info["Email"] = self.user.email
        info["Joined"] = self.user.created_at
        
        return '\n'.join([f"{info_item[0]}: {info_item[1]}" for info_item in info.items()])
