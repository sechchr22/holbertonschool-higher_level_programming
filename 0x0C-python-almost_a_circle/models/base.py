#!/usr/bin/python3
"""
Base Class
"""
import json


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

    def to_json_string(list_dictionaries):
        """
        json to list
        Args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save instance to a file
        Args:
            cls: class
            list_objs: 
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

        with open('{}'.format(filename), 'a+', encoding='utf-8') as a_file:
            json.dump(list_of_json_objs, a_file)

    @classmethod
    def create(cls, **dictionary):

        key_word = 'size'
        signal = 'Square not found'

        dummy_square = cls(1, 2, 3)
        dummy_rectangle = cls(1, 2, 3, 4)

        for key in dictionary:
            if key == key_word:
                signal = 'Square found'
                dummy_square.update(**dictionary)
                break

        if signal == 'Square not found':
            dummy_rectangle.update(**dictionary)
            return dummy_rectangle

        else:
            return dummy_square

    @classmethod
    def load_from_file(cls):

        list_of_instances = []
        filename = '{}.json'.format(cls.__name__)

        with open('{}'.format(filename), 'r', encoding='utf-8') as a_file:
            line = a_file.readline()

        list_of_instances_json = cls.from_json_string(line)

        for instance_dict in list_of_instances_json:
            new_instance = cls.create(**instance_dict)
            list_of_instances.append(new_instance)

        return list_of_instances

    @staticmethod
    def from_json_string(json_string):

        if len(json_string) is 0:
            return []

        return json.loads(json_string)
