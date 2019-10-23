#!/usr/bin/python3
"""Importing Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """size property"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value

    def update(self, *args, **kwargs):
        """update instance"""
        attribute = ['id', 'size', 'x', 'y']
        i = 0

        if args is not None and len(args) != 0:
            for arg in args:
                setattr(self, attribute[i], arg)
                i += 1
        else:
            for kwarg in kwargs:
                for attr in attribute:
                    if kwarg == attr:
                        setattr(self, attr, kwargs[kwarg])

    def to_dictionary(self):
        """instance to dictionary"""
        attribute = ['id', 'size', 'x', 'y']
        _dic = {}
        for attr in attribute:
            _dic[attr] = getattr(self, attr)
        return _dic
