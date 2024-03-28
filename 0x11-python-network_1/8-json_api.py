#!/usr/bin/python3
"""
Module to send a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    """
    Takes in a letter, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter, and displays the response.
    If the response body is properly JSON formatted and not empty, displays the id and name.
    Otherwise, displays "Not a valid JSON" if the JSON is invalid, and "No result" if the JSON is empty.
    """
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}
    response = requests.post(url, data=payload)

    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
