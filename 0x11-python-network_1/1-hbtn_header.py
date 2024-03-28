#!/usr/bin/python3
"""
Module to fetch the value of the X-Request-Id variable from the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    """
    Takes in a URL, sends a request to the URL, and displays the value of the X-Request-Id variable found in the header of the response.
    """
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
