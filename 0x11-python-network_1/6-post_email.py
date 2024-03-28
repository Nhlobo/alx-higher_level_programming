#!/usr/bin/python3
"""
Module to send a POST request with an email as a parameter and display the body of the response using the requests package.
"""

import requests
import sys

if __name__ == "__main__":
    """
    Takes in a URL and an email, sends a POST request to the URL with the email as a parameter, and displays the body of the response.
    """
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
