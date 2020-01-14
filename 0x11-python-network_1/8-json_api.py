#!/usr/bin/python3
'''
Python script that takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

import requests
import sys

if __name__ == '__main__':

    values = {}
 
    if len(sys.argv) != 1:
        values['q'] = sys.argv[1]
    else:
        values['q'] = ""

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', data=values) 
        dictio = r.json()
       
        if len(dictio) > 0:
            print('[{}] {}'.format(dictio['id'], dictio['name']))

        else:
            print('No result')

    except Exception as any_error:
        print('Not a valid JSON') 
