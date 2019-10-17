#!/usr/bin/python3
"""Class Student"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves dictionary representation of instace

        Args:
            attrs: list choosing what attributes to show
        """
        dictionary = self.__dict__

        new_dict = {}

        if attrs is not None:
            for attribute in attrs:
                if attribute in dictionary:
                    new_dict[attribute] = dictionary[attribute]
            if bool(new_dict) is False:
                return dictionary
            else:
                return new_dict
        else:
            return dictionary

    def reload_from_json(self, json):
        """
        To set attributes of the instance

        Args:
            json: Dictionary
        """
        keys = list(json.keys())
        for key in keys:
            self.key = json[key]
