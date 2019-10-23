#!/usr/bin/python3
"""importing Base class"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):

        attribute = ['id', 'width', 'height', 'x', 'y']
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
        attribute = ['id', 'width', 'height', 'x', 'y']
        _dic = {}
        for attr in attribute:
            _dic[attr] = getattr(self, attr)
        return _dic
