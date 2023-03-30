#!/bin/bash
# sends a GET request to URL ...
# display the body of the response {if statusCode === 200}

curl -G -L -s -o /dev/null -w "%{http_code}" $1 | grep -q 200 && curl -L -s $1 
