#!/usr/bin/python3

import sys
import requests


if __name__ == "__main__":
    from sys import argv
    import requests

    req = requests.get(argv[1])
    print(req.headers.get("X-Request-Id"))
