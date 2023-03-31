#!/usr/bin/python3
"""
    Python script that takes in a URL, \
        sends a request to the URL
"""
import urllib.request


def main(_arg):
    """
    sends a request to the URL and displays the value \
    of the `X-Request-Id` variable found in the header \
    of the response
    rtype: uint
    """
    _link = urllib.request.Request(_arg)
    with urllib.request.urlopen(_link) as read_url:
        print(dict(read_url.headers).get("X-Request-Id"))


if __name__ == "__main__":
    from sys import argv
    main(argv[1])
