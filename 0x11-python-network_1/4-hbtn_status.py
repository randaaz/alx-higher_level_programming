#!/usr/bin/python3
"""
Python script that fetches the status of the URL
'https://alx-intranet.hbtn.io/status'
using the requests package.
"""
import requests


if __name__ == "__main__":
    requ = requests.get('https://alx-intranet.hbtn.io/status')
    te = requ.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(te), te))
