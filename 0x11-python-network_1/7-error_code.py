#!/usr/bin/python3
"""A Python script that takes a URL as a command-line argument,
sends an HTTP GET request to the specified URL using the requests
package, and prints the body of the response. If the HTTP status
code is greater than or equal to 400, it prints an error message
along with the status code.

Usage:
    $ ./7-error_code.py https://example.com
"""
import sys
import requests


if __name__ == "__main__":
    path = sys.argv[1]

    requ = requests.get(path)
    if requ.status_code >= 400:
        print("Error code: {}".format(requ.status_code))
    else:
        print(requ.text)
