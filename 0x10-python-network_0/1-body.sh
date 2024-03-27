#!/bin/bash
# This script takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

URL=$1

# Send a request to the URL and get the body size using curl
SIZE=$(curl -sI "$URL" | grep -i Content-Length | awk '{print $2}')

echo "$SIZE"
