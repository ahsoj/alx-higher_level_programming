#!/usr/bin/python3
"""
     Python script that fetches\
             https://alx-intranet.hbtn.io/status
"""
import requests


def main():
    """
        fetch `https://alx-intranet.hbtn.io/status`
        rtype: str
    """
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == "__main__":
    main()
