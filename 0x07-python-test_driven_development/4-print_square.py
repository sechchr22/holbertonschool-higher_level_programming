#!/usr/bin/python3

"""
print_square

prints a square with the character #

or raise an exception otherwise
"""


def print_square(size):

    """
    Args:
        size: length of the square

    Returns:
        nothing just ends printing the square
    """

    if type(size) != int:
        if type(size) is float and size < 0:
            raise TypeError('size must be an integer')
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
