#!/usr/bin/python3
import requests


req = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
print(f"\t- type: {type(req.text)}")
print(f"\t- content: {req.text}")
