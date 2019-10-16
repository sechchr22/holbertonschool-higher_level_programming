#!/usr/bin/python3
"""Module my_int"""


class MyInt(int):
    """class MyInt"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, obj):
        """inverted equal"""
        if isinstance(obj, MyInt):
            return self.value == other.value
        return False

    def __ne__(self, obj):
        """Inverted non equal"""
        return not self.__eq__(obj)
