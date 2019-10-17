#!/usr/bin/python3
"""Write into file module"""


def write_file(filename="", text=""):
    """
    To writte into a file

    Create it if it doesnt exist

    Args:
        filename: string containing filename
        text: string to be writted into file

    Return:
          number of characters writted
    """

    with open('{}'.format(filename), 'w+', encoding='utf-8') as a_file:
        a_file.write(text)
        return len(text)
