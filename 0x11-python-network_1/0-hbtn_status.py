#!/usr/bin/python3
'''
Python module to fetch an URL
'''

import urllib.request

url = 'https://intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    html = response.read()
    print('Body response:\n\t- type: \
{}\n\t- content: {}\n\t- utf8 content: {}'.
          format(type(html), html, str(html.decode('utf-8')))
          )
