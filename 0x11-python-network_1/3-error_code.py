#!/usr/bin/python3
"""A Python script that takes a URL as a command-line
argument, sends an HTTP GET request to the specified
URL using the urllib package, and prints the body of the
response. If an HTTP error occurs, it prints the error code.

Usage:
    $ ./3-error_code.py http://example.com
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as req:
            print(req.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
