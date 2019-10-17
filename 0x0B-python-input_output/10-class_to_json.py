#!/usr/bin/python3
"""
returns the dictionary description for
for JSON serialization of an object module
"""


def class_to_json(obj):
    """
    To have a dictionary description of an
    object for JSON serialization

    Args:
        obj: object

    Return:
        Dictionary with the description of the object
    """

    return obj.__dict__
