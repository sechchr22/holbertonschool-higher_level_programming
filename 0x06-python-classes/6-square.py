#!/usr/bin/python3
class Square:
    """
    Square Class
    Args:
         size: just the size of the square indexed by user
    Attributes:
        _Square__size: square size
    """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) == tuple and len(position) == 2:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """
        Wanna know the coordenate?
        Return: position
        """
        return(self.__position)

    @position.setter
    def position(self, value):
        """
        Position setter
        Args:
            value: position value
        """
        if type(value) == tuple and len(value) == 2 \
                and value[0] > 0 and value[1] > 0 \
                and type(value[0]) is int and type(value[1]) is int:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            for k in range(0, self.__position[0]):
                print("{}".format(" "), end="")
            for j in range(0, self.__size):
                print("{:s}".format("#"), end="")
            print()
