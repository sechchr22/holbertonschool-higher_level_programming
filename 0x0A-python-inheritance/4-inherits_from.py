#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """
    To check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: instance
        a_class: class

    Returns: True or false
    """

    if type(obj) is a_class:
        return(False)
    elif issubclass(type(obj), a_class):
        return(True)
    else:
        return(False)
