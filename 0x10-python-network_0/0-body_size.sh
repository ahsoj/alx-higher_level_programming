#!/bin/bash
# send a request to url & display byte data ...
curl -G -s -o /dev/null -w '%{size_download}\n' $1
