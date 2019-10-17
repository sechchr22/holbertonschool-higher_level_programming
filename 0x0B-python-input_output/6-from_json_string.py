#!/usr/bin/python3
"""Decoding a json format module"""

import json


def from_json_string(my_str):
    """
    To decode a json format to generate an object

    Args:
        my_str: string in json format

    Return:
        object generated with the decodification of
        Json format
    """
    return json.loads(my_str)
