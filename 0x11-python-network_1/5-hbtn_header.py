#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request \
        to the URL and displays the value of the variable
 """


if __name__ == "__main__":
    from sys import argv
    import requests

    req = requests.get(argv[1])
    print(req.headers.get("X-Request-Id"))
