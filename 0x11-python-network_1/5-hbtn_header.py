#!/usr/bin/python3
'''
python module hat fetches https://intranet.hbtn.io/status
using requests package
'''

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers['X-Request-Id'])
