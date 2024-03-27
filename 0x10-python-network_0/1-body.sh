#!/bin/bash
# This script takes in a URL, sends a GET request to the URL,
# and displays the body of the response if the status code is 200

URL=$1

# Send a GET request to the URL and display the body if the status code is 200
curl -s -X GET -L -w "%{http_code}" "$URL" -o /dev/null | 
if [ $(cat -) -eq 200 ]; then
    curl -s "$URL"
fi
