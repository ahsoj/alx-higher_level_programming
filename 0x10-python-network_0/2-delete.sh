#!/bin/bash
#send a DELETE request of the URL passed as a first argument...
# display the body of the response

curl -s -X DELETE $1
