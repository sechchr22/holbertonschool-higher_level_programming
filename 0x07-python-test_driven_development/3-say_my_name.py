#!/usr/bin/python3

"""
say_my_name module

prints My name is <first name> <last name>

or it raise an exception otherwise

"""


def say_my_name(first_name, last_name=""):

    """
    Args:
        first_name: first name, must be an string
        last_name: last name, must be an string

    Returns:
        Nothing, this functions just ends printing the complete name
    """

    if type(first_name) != str:
        raise TypeError('first_name must be a string')
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    else:
        print("My name is {} {}".format(first_name, last_name))
