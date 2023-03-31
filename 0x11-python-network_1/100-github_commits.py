#!/usr/bin/python3
"""
    Holberton School staff
"""
import requests


def main(arg1, arg2):
    """
        Python script that takes 2 arguments in \
                order to solve this challenge.
    """
    url = f"https://api.github.com/repos/{arg1}/{arg2}/commits"

    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass


if __name__ == "__main__":
    from sys import argv
    main(argv[1], argv[2])
