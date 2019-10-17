#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """
    To read file and print it

    Args:
        filename: string with file name
    """
    with open('{}'.format(filename)) as a_file:
        for line in a_file:
            print(line, end="")
