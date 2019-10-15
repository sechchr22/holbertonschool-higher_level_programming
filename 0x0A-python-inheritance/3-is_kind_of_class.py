#!/usr/bin/python3
"""Is kind of class module"""


def is_kind_of_class(obj, a_class):
    """
    To check if an object belongs to a class

    Args:
        Obj: instance
        a_class: class

    Returns:
        True if the object belongs to the class
        False otherwise
    """

    return isinstance(obj, a_class)
