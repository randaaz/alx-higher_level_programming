#!/usr/bin/python3
"""defines a square"""


class Square:
    """Represents Square class."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: if the size is not integer
            ValueError: if the size less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
