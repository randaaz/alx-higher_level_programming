#!/usr/bin/python3
"""Inheritance class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inheritance class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """the area of the Square"""
        return self.__size ** 2
