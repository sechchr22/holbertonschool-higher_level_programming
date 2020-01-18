#!/usr/bin/python3
'''
python module that takes my Github credentials
and uses Github API to display my id
'''

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    try:

        r = requests.get(
            'https://api.github.com/user',
            auth=HTTPBasicAuth(
                sys.argv[1],
                sys.argv[2]))

        Dict = r.json()
        print(Dict['id'])

    except Exception as error:
        print('None')
