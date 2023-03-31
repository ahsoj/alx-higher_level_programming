#!/usr/bin/python3
"""
    Python script that takes in a URL
"""
import requests


def main(_arg):
    """
    sends a request to the URL and displays \
    the body of the response.
    """
    req = requests.get(_arg)
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)


if __name__ == "__main__":
    from sys import argv
    main(argv[1])
