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
    sp = ' '
    print("Body response:")
    print(f"{sp*4}- type: {type(req.text)}")
    print(f"{sp*4}- content: {req.text}")


if __name__ == "__main__":
    main()
