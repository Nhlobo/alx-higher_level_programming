#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL,
# and displays the body of the response. It sends a header variable X-School-User-Id with the value 98.

URL=$1

# Send a GET request to the URL with the header variable X-School-User-Id set to 98
curl -s -X GET -H "X-School-User-Id: 98" "$URL"
