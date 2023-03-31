#!/usr/bin/python3
"""
    Python script that takes in a URL and an email
"""
import urllib.request, urllib.parse


def main(arg1, arg2):
    """
    sends a POST request to the passed URL with the email \
            as a parameter, and displays the body of the \
            response (decoded in utf-8)
    """
    data = {"email": arg2}
    _data = urllib.parse.urlencode(data).encode("ascii")

    _link = urllib.request.Request(arg1, _data)
    with urllib.request.urlopen(_link) as read_url:
        print(read_url.read().decode("utf-8"))


if __name__ == "__main__":
    from sys import argv
    main(argv[1], argv[2])
