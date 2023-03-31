#!/usr/bin/python3
import requests


if __name__ == "__main__":
    req = requests.get("https://intranet.hbtn.io/status")
    sp = ' '
    print("Body response:")
    print(f"{sp*4}- type: {type(req.text)}")
    print(f"{sp*4}- content: {req.text}")
