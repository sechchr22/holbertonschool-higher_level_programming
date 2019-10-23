#!/usr/bin/python3
"""
Base Class
"""
import json
import os


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        to inizializate an instance
        Args:
            id: integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        json to list
        Args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save instance to a file
        """
        attributes = ['width', 'height', 'size', 'x', 'y', 'id']
        list_of_json_objs = []

        for obj in list_objs:

            _dict = {}

            dict_1 = obj.__dict__
            keys = list(dict_1.keys())

            for key in keys:
                for attr in attributes:
                    if key.find(attr) != -1:
                        _dict[attr] = getattr(obj, attr)

            list_of_json_objs.append(_dict)

        filename = '{}.json'.format(cls.__name__)

        with open('{}'.format(filename), 'w', encoding='utf-8') as a_file:
            a_file.write(cls.to_json_string(list_of_json_objs))

    @classmethod
    def create(cls, **dictionary):
        """
        to create an instance
        from a dictionary
        """

        if cls.__name__ == 'Square':
            dummy = cls(1)
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 2)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load instance from a file"""

        list_of_instances = []
        filename = '{}.json'.format(cls.__name__)

        if os.path.exists(filename) is False:
            return list_of_instances

        with open('{}'.format(filename), 'r', encoding='utf-8') as a_file:
            if a_file is None:
                return []
            line = a_file.readline()

        list_of_instances_json = cls.from_json_string(line)

        for instance_dict in list_of_instances_json:
            new_instance = cls.create(**instance_dict)
            list_of_instances.append(new_instance)

        return list_of_instances

    @staticmethod
    def from_json_string(json_string):
        """from json to string"""

        if json_string is None or len(json_string) is 0:
            return []

        return json.loads(json_string)
