#!/usr/bin/python3

import math


class MagicClass:
    """Represents a MagicClass with radius-based calculations."""
    def __init__(self, radius=0):
        """
        Initializes a new instance of the MagicClass.

        Args:
            radius (int or float, optional): The radius of the magic circle.
                Defaults to 0.

        Raises:
            TypeError: If the radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Computes the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return (self.__radius ** 2 * math.pi)

    def circmference(self):
        """
        Computes the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return (* math.pi * self.__radius)
