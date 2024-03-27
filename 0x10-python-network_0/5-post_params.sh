#!/bin/bash
# This script takes in a URL, sends a POST request to the passed URL,
# and displays the body of the response. It sends variables email and subject with predefined values.

URL=$1

# Send a POST request to the URL with the specified parameters
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$URL"
