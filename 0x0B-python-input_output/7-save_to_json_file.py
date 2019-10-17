#!/usr/bin/python3
"""Save object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """
    To save an object into a file

    Args:
        my_obj: object
        filename: file to save the object

    """

    with open('{}'.format(filename), 'w+', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
