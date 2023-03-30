#!/bin/bash
# take in a URL & display all HTTP methods Allowed
curl -s -i -X OPTIONS $1 | grep Allow | cut -d ':' -f 2- | sed 's/^[[:space:]]*//'
