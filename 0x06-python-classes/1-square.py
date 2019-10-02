#!/usr/bin/python3
class Square:

    """
    Square with its size being private

    Args:
        size: just the size of the square indexed by user

    Attributes:
        _Square__size: square size
    """

    def __init__(self, size):
        self.__size = size
