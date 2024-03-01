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
        con = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(con)))
        print("\t- content: {}".format(con))
        print("\t- utf8 content: {}".format(con.decode('utf-8')))
