#!/usr/bin/python3
"""
    Python script that takes in a URL and an email address,
"""
import requests


def main(arg1, arg2):
    """
         sends a POST request to the passed URL with the \
            email as a parameter, and finally displays the \
            body of the response.
    """
    data = {"email": arg2}
    req = requests.post(arg1, data)
    print(req.text)


if __name__ == "__main__":
    from sys import argv
    main(argv[1], argv[2])
