#!/usr/bin/python3
'''
Python module to sends a request to the URL and
displays the value of the X-Request-Id variable
'''

import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        print(response.info()['X-Request-Id'])
