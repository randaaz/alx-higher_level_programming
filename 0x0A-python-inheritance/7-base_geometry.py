#!/usr/bin/python3
""" define class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Exception:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
            """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
