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

    """class attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
        """
        To print rectangle with #
        Returns: square with #, or empty one if width or
        height is equal to 0
        """
        i = 0
        chain = ""
        symbol = str(self.print_symbol)

        if self.__height is 0 or self.__width is 0:
            return chain

        while (i < self.__height):
            j = 0
            while(j < self.__width):
                chain += symbol
                j += 1
            if i != (self.__height - 1):
                chain += "\n"
            i += 1

        return chain

    def __repr__(self):
        """
        To print rectangle with #
        Returns: square with #, or empty one if width or
        height is equal to 0
        """
        width = str(self.__width)
        height = str(self.__height)
        chain = "Rectangle"+"("+width+","+" "+height+")"
        return chain

    def __del__(self):
        """
        To delete an instance
        """
        Rectangle.number_of_instances -= 1
        print('Bye Rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        To compare areas between 2 rectangles
        Args:
            rect_1: Rectangle instace
            rect_2: Rectangle instace
        Returns:
            rect_1 if areas are equal or rect_1 has the biggest area
            rect_2 otherwise
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() == rect_2.area():
            return(rect_1)
        elif rect_1.area() > rect_2.area():
            return(rect_1)
        else:
            return(rect_2)

    @classmethod
    def square(cls, size=0):
        """
        To create a new instance where
        width == height == size
        """
        return cls(size, size)
