#!/usr/bin/python3
"""Number of lines module"""


def number_of_lines(filename=""):
    """To return number of lines o a file"""

    line_counter = 0

    with open('{}'.format(filename), 'r', encoding='utf-8') as a_file:
        for line in a_file:
            line_counter += 1

    return line_counter
