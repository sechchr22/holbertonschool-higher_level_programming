#!/usr/bin/python3
"""Read n lines module"""


def read_lines(filename="", nb_lines=0):
    """To read n line from a file"""
    with open('{}'.format(filename), 'r', encoding='utf-8') as a_file:
        i = 0
        for line in a_file:
            if i == nb_lines and i > 0:
                break
            elif i == 0 or i <= 0:
                pass
            print(line, end="")
            i += 1
