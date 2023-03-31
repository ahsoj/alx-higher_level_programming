#!/usr/bin/python3
import requests


req = requests.get("https://intranet.hbtn.io/status")
sp = ' '
print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
