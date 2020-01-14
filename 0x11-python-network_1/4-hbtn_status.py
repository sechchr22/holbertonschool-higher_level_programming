#!/usr/bin/python3
'''
python module hat fetches https://intranet.hbtn.io/status
using requests package
'''

import requests

if __name__ == "__main__":

    r = requests.get('https://intranet.hbtn.io/status')
    print('Body response:\n\t- type: {}\n\t- content: {}'.
          format(type(r.text), r.text)
          )
