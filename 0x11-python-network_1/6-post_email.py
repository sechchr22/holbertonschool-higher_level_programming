#!/usr/bin/python3
'''
python module that send a POST request with a parameter
and displays the body of the response
'''

import requests
import sys

if __name__ == "__main__":

    values = {'email': sys.argv[2]}

    try:
        r = requests.post(sys.argv[1], data=values)
        print(r.text)
    except BaseException:
        pass
