#!/usr/bin/python3
import json


class Base:
    """
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

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
