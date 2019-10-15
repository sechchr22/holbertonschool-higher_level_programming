#!/usr/bin/python3
class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """Just raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """To validate value"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
