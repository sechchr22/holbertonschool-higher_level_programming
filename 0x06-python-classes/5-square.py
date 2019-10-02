#!/usr/bin/python3
class Square:
    """
    Square Class
    Args:
         size: just the size of the square indexed by user
    Attributes:
        _Square__size: square size
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Want to know the size of the square?
        Return:
            square size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size setter
        Args:
            value: argument indexed as square size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Wanna get the area of the square? here it is
        Returns:
            square area
        """
        return (self.__size**2)

    def my_print(self):
        """print square"""
        if self.__size is 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("{:s}".format("#"), end="")
            print()
