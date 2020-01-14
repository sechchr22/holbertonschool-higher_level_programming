#!/usr/bin/python3
'''
Python module to sends a request to the URL and
displays the value of the X-Request-Id variable
'''

import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(str(html.decode('utf-8')))
