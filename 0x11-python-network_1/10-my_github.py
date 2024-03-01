#!/usr/bin/python3
"""A Python script that takes GitHub credentials
(username and personal access token) as command-line arguments,
uses Basic Authentication to access the GitHub API,
and displays the user's ID.

Usage:
    $ ./10-my_github.py <username> <personal_access_token>
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    requ = requests.get("https://api.github.com/user", auth=auth)
    print(requ.json().get("id"))
