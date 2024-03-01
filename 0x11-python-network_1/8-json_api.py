#!/usr/bin/python3
"""A Python script that takes a letter as a
command-line argument (optional), sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter,
and prints the id and name if the response body is properly JSON
formatted and not empty. Otherwise, it prints "Not a valid JSON"
if the JSON is invalid, or "No result" if the JSON is empty.

Usage:
    $ ./8-json_api.py
    $ ./8-json_api.py a
    $ ./8-json_api.py 2
    $ ./8-json_api.py b
"""
import sys
import requests


if __name__ == "__main__":
    lt = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": lt}

    requ = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = requ.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
