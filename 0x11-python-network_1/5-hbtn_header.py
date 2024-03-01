#!/usr/bin/python3
"""A Python script that takes a URL as a command-line argument,
sends an HTTP GET request to the specified URL using the requests
package, and prints the value of the 'X-Request-Id' variable
in the response header.

Usage:
    $ ./5-hbtn_header.py https://example.com
"""
import sys
import requests


if __name__ == "__main__":
    path = sys.argv[1]

    requ = requests.get(path)
    print(requ.headers.get("X-Request-Id"))
