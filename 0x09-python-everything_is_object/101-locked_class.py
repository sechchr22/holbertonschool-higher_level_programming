#!/usr/bin/python3
"""Locked Class"""


class LockedClass:
    """
    Locked class

    Just can create an attribute if its name is
    "first_name"
    """
    __slots__ = "first_name"
