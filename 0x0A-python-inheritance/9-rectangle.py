#!/usr/bin/python3
"""Inheritance class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inheritance class"""
    def __init__(self, width, height):
        """Inheritance class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """rectangle description"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
