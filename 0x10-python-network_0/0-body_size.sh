#!/bin/bash
# send a request to url ...
# display the size of response body with byte

curl -s -o /dev/null -w '%{size_download}\n' $1
