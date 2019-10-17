#!/usr/bin/python3
"""Append into file module"""


def append_write(filename="", text=""):
    """
    To append into a file

    Create it if it doesnt exist

    Args:
        filename: string containing filename
        text: string to be writted into file

    Return:
          number of characters appended
    """

    with open('{}'.format(filename), 'a+', encoding='utf-8') as a_file:
        a_file.write(text)
        return len(text)
