#!/usr/bin/python3
class Rectangle:

    """
    Rectangle with width and height attributes
    
    Args:
        width: width of the rectangle must be an integer
        height: height of the rectangle must be an integer

    Attributes:
        width
        height
    """

    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    """
    To know rectangle´s width

    Return: rectangle´s width attribute    
    """
    def width(self):
        return(self.__width)

    @width.setter
    """
    To set rectangle´s width
    
    Args:
        value: must be an integer
    """
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    """
    To know rectangle´s height

    Return: rectangle´s height attribute
    """
    def height(self):
        return(self.__height)

    @height.setter
    """
    To set rectangle´s height

    Args:
        value: must be an integer
    """
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
