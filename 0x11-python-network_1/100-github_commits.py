#!/usr/bin/python3
"""A Python script that takes GitHub repository owner
and name as command-line arguments, uses the GitHub API to
fetch the latest 10 commits, and prints the SHA and
author name for each commit.

Usage:
    $ ./100-github_commits.py <owner> <repo_name>
"""
import sys
import requests


if __name__ == "__main__":
    path = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    requ = requests.get(path)
    commits = requ.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
