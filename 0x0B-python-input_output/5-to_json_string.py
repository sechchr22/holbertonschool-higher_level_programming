#!/usr/bin/python3
"""Jsonized data module"""

import json


def to_json_string(my_obj):
    """
    To jsonized data

    Args:
        my_obj: object

    Return:
        Data in json format
    """

    return json.dumps(my_obj)
