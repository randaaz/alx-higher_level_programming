#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


"""Inheritance class"""


class Square(Rectangle):
    """Inheritance class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Square description"""
        return "[Rectangle] " + str(self.__size) + "/" + str(self.__size)
