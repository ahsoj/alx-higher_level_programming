#!/bin/bash
# take in a URL & display all HTTP methods Allowed
curl -X OPTIONS $1
