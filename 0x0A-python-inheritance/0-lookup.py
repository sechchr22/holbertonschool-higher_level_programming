#!/usr/bin/python3
"""
Look up module

returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj: class

    Returns:
        list of available attributes and methos
    """
    return dir(obj)
