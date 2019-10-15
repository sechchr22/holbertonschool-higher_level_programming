#!/usr/bin/python3
"""
my_list module

Subclass MyList from class list

print_sorted method
"""


class MyList(list):

    """Subclass Mylist from list"""

    def print_sorted(self):

        """To print sorted list"""

        new = self.copy()
        new.sort()
        print(new)
