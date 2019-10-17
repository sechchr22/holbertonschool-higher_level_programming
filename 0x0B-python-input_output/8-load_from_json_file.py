#!/usr/bin/python3
"""creates an Object from a JSON file module"""

import json


def load_from_json_file(filename):
    """
    To create an object stored in a file in
    Json format

    Args:
        filename: string with filename

    Return:
        object created
    """

    with open('{}'.format(filename), 'r', encoding='utf-8') as a_file:
        return json.load(a_file)
