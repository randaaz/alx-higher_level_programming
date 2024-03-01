#!/usr/bin/python3
"""A Python script that takes a URL and an
email as command-line arguments, sends an HTTP
POST request to the specified URL using the urllib
package with the email as a parameter,
and prints the body of the response.

Usage:
    $ ./2-post_email.py http://example.com/post_email user@example.com
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    path = sys.argv[1]
    v = {"email": sys.argv[2]}
    d = urllib.parse.urlencode(v).encode("ascii")

    request = urllib.request.Request(path, d)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
