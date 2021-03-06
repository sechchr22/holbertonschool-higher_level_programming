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
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        To know rectangle´s width
        Return: rectangle´s width attribute
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """
        To set rectangle´s width
        Args:
            value: must be an integer
         """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        To know rectangle´s height
        Return: rectangle´s height attribute
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """
        To set rectangle´s height
        Args:
            value: must be an integer
        """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
