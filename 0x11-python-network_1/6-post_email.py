#!/usr/bin/python3
"""A Python script that takes a URL and an email as
command-line arguments, sends an HTTP POST request to the specified
URL using the requests package with the email as a parameter, and
prints the body of the response.

Usage:
    $ ./6-post_email.py http://example.com/post_email user@example.com
"""
import sys
import requests


if __name__ == "__main__":
    path = sys.argv[1]
    v = {"email": sys.argv[2]}

    requ = requests.post(path, data=v)
    print(requ.text)
