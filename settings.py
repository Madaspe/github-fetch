import os
import getpass

print(f"/home/{getpass.getuser()}/.config/github-fetch/token")

TOKEN = None

try:
    with open(f"/home/{getpass.getuser()}/.config/github-fetch/token", "r") as file:
       TOKEN = file.read().replace("\n", "")
except Exception as e:
    print(e)
    print("Not token file. Please create file with github Token. File path shoud be ~/.config/github-fetch/token")
    exit(0)
