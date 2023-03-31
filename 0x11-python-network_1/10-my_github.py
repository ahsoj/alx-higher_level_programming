#!/usr/bin/python3
"""
    Python script that takes your GitHub credentials
"""
import requests
from requests.auth import HTTPBasicAuth


def main(arg1, arg2):
    """
        GitHub credentials (username and password) \
            and uses the GitHub API to display your id
    """
    auth = HTTPBasicAuth(arg1, arg2)
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))


if __name__ == "__main__":
    from sys import argv
    main(argv[1], argv[2])
