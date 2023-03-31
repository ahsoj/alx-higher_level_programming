#!/usr/bin/python3
import requests


req = requests.get("https://intranet.hbtn.io/status")
sp = ' '
print("Body response:")
print(f"{sp*4}- type: {type(req.text)}")
print(f"{sp*4}- content: {req.text}")
