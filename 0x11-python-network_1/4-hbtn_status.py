#!/usr/bin/python3
"""
    Python script that fetches \
    https://alx-intranet.hbtn.io/status
    rtype: str
"""


if __name__ == "__main__":
    import requests
    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(req.text)}")
    print(f"\t- content: {req.text}")
