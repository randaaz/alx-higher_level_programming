#!/usr/bin/python3
"""defines a square"""


class Square:
    """Represents Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
            position (int): The position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method to set the size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the size is not an integer.
             ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Setter method to set the position.

        Args:
            value (int): The position.

        Raises:
            TypeError: If position not be a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Printing same behavior as my_print()."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.size):
            [print(" ", end="") for r in range(0, self.__position[0])]
            [print("#", end="") for c in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
