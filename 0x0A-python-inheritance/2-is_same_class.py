#!/usr/bin/python3
"""Same class Module"""


def is_same_class(obj, a_class):

    """
    To know if an object belongs EXACTLY to a class

    Args:
        obj: instance

        a_class: class

    Return:
        True if exactly belongs, false otherwise
    """

    if type(obj) is a_class:
        return True
    else:
        False
