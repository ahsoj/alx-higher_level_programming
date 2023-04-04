#!/usr/bin/python3
"""
    Python script that fetches \
        https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    """
    Python script that fetches \
        https://alx-intranet.hbtn.io/status
    """
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
