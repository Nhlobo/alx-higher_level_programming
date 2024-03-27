#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument
# and displays the body of the response

URL=$1

# Send a DELETE request to the URL and display the body of the response
curl -s -X DELETE "$URL"
