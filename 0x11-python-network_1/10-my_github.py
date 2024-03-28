#!/usr/bin/python3
"""
Module to use the GitHub API to display the user's id using Basic Authentication with a personal access token.
"""

import requests
import sys

if __name__ == "__main__":
    """
    Takes in the GitHub username and personal access token as arguments, and uses the GitHub API to display the user's id.
    """
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    try:
        data = response.json()
        print(data.get('id'))
    except ValueError:
        print("None")
