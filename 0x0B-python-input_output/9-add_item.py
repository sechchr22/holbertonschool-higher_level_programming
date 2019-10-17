#!/usr/bin/python3
import sys
import json
import os.path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if os.path.exists('add_item.json') == False:
    empty_list = []
    save_to_json_file(empty_list, 'add_item.json')

else:
    current_list = load_from_json_file('add_item.json')
    for i in range(1, len(sys.argv)):
        current_list.append(sys.argv[i])
        save_to_json_file(current_list, 'add_item.json')
