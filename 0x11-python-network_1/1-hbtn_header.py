#!/usr/bin/python3
"""A Python script that takes a URL as a
command-line argument, sends an HTTP GET request
to the specified URL using the urllib package, and
prints the value of the 'X-Request-Id' variable
found in the response header.

Usage:
    $ ./1-hbtn_header.py https://example.com
"""
import sys
import urllib.request

if __name__ == "__main__":
    path = sys.argv[1]

    request = urllib.request.Request(path)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
