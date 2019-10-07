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

    def area(self):
        """
        To calculate rectangle´s area
        
        Returns: rectangle´s area
        """
        return(self.__height * self.__width)

    def perimeter(self):
        """
        To calculate rectangle´s perimeter

        Returns: if height or widht is equal to 0, returns 0

        rectangle´s area otherwise
        """
        if self.__height is 0 or self.__width is 0:
            return(0)
        a = 2 * self.__height
        b = 2 * self.__width
        return(a + b)

    def __str__(self):
       """To print rectangle with #"""
       i = 0
       chain = ""
       while (i < self.__height):
           j = 0
           while( j < self.__width):
               chain += "#"
               j += 1
           if i != (self.__height - 1):
               chain += "\n"
           i += 1
       return chain
