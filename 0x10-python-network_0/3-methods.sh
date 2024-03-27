#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept

URL=$1

# Send an OPTIONS request to the URL and display the allowed methods
curl -s -i -X OPTIONS "$URL" | grep "Allow:" | cut -d ' ' -f 2-
