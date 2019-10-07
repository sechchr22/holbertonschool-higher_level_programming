#!/usr/bin/python3

"""
text_indentation module

function that prints a text with 2 new
lines after each of these characters: ., ? and :

or raise an exception otherwise
"""


def text_indentation(text):

    """
    Args:
        text: must be a string

    Returns: nothing, just prints the whole text
    """

    if type(text) != str:
        raise TypeError('text must be a string')

    i = 0

    while i < (len(text) - 1):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i], end="")
            print()
            print()
            if text[i + 1] == " " and text[i + 2] is not None:
                i += 2
            else:
                i += 1
        else:
            print(text[i], end="")
            i += 1
    if text[i] == "." or text[i] == "?" or text[i] == ":":
        print(text[i], end="")
        print()
    else:
        print(text[i], end="")
