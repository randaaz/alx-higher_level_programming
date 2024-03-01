# 0x11. Python - Network #1

## Project Description

This repository contains Python scripts for various network-related tasks. The project is part of the curriculum at Holberton School and is designed to enhance your understanding of fetching internet resources using the `urllib` and `requests` packages, handling HTTP requests, decoding responses, and working with APIs.

## Learning Objectives

Upon completion of this project, you are expected to be able to explain the following without relying on external sources:

### General
- How to fetch internet resources with the Python package `urllib`
- How to decode `urllib` body response
- How to use the Python package `requests` (`#requestsiswaysimplerthanurllib`)
- How to make HTTP GET requests
- How to make HTTP POST/PUT/etc. requests
- How to fetch JSON resources
- How to manipulate data from an external service

## Copyright - Plagiarism

You are responsible for finding solutions to the tasks to meet the learning objectives. Copying and pasting someone else’s work is strictly forbidden and will result in removal from the program. Do not publish any content from this project.

## Requirements

### General

- Allowed Editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- Your code should use the `pycodestyle` (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- Use `get` to access dictionary values by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method (the length will be verified)
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Tasks

```bash
# 0. What's my status? #0
./0-hbtn_status.py

# 1. Response header value #0
./1-hbtn_header.py https://alx-intranet.hbtn.io

# 2. POST an email #0
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

# 3. Error code #0
./3-error_code.py http://0.0.0.0:5000
./3-error_code.py http://0.0.0.0:5000/status_401
./3-error_code.py http://0.0.0.0:5000/doesnt_exist
./3-error_code.py http://0.0.0.0:5000/status_500

# 4. What's my status? #1
./4-hbtn_status.py

# 5. Response header value #1
./5-hbtn_header.py https://alx-intranet.hbtn.io

# 6. POST an email #1
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com

# 7. Error code #1
./7-error_code.py http://0.0.0.0:5000
./7-error_code.py http://0.0.0.0:5000/status_401
./7-error_code.py http://0.0.0.0:5000/doesnt_exist
./7-error_code.py http://0.0.0.0:5000/status_500

# 8. Search API
./8-json_api.py
./8-json_api.py a
./8-json_api.py 2
./8-json_api.py b

# 9. My GitHub!
./10-my_github.py papamuziko cisfun
./10-my_github.py papamuziko wrong_pwd

# advanced tasks
1 advanced tasks
