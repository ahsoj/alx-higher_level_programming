#!/usr/bin/python3
"""
    Python script that takes in a URL
"""
from urllib import request, error


def main(_arg):
    """
     sends a request to the URL and displays the \
             body of the response (decoded in utf-8).
    """
    try:
        with request.urlopen(_arg) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)


if __name__ == "__main__":
    from sys import argv
    main(argv[1])
