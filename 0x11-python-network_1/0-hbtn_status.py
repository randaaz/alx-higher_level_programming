#!/usr/bin/python3
"""The script sends an HTTP GET request to the specified URL,
retrieves the response, and prints information about the response body.
- The type of the content (class 'bytes').
- The raw content of the response.
- The content decoded in UTF-8.
"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
