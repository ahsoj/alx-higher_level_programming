#!/usr/bin/python3
"""
   Python script that fetches \
   The body of the response must be display \
   like the following example (tabulation before -)
"""
import requests


req = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
print(f"\t- type: {type(req.text)}")
print(f"\t- content: {req.text}")
