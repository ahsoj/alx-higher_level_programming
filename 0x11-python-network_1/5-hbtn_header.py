#!/usr/bin/python3

from sys import argv
import requests

req = requests.get(argv[1])
print(req.headers.get("X-Request-Id"))
