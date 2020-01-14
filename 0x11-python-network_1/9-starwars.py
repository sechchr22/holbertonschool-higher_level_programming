#!/usr/bin/python3
'''
python module hat fetches https://intranet.hbtn.io/status
using requests package
'''

import requests
import sys

if __name__ == "__main__":

    search_string = '?search=' + sys.argv[1]
    r = requests.get('https://swapi.co/api/people/{}'.format(search_string))
    request = r.json()

    print('Number of results: {}'.format(request['count']))

    results = request['results']
    for i in range(0, len(results)):

        print(results[i]['name'])
