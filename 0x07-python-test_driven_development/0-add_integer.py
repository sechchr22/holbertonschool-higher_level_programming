#!/usr/bin/python3

"""
Add integer module

This module contains a function that adds 2 integers

it returns the addition of the 2 integers or an exception
will be raised otherwise.

"""


def add_integer(a, b=98):

    """
    Args:
        a: integer/float
        b: integer/float

    Returns: a + b
    """

    if type(a) == int or type(a) == float:
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) == int or type(b) == float:
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    return a + b
