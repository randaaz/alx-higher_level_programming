#!/usr/bin/python3
"""A class Rectangle"""


class Rectangle:
    """defines a rectangle"""

    number_of_instances = 0
    """int: public attribute representing the number of instances."""

    print_symbol = '#'
    """type: representing the symbol used for string representation."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """prints in stdout the square with the character #"""
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") *
                self.__height)[:-1]

    def __repr__(self):
        """representation of the rectangle"""
        x = str(self.__height)
        return "Rectangle(" + str(self.__width) + ", " + x + ")"

    def __del__(self):
        """Print the message Bye rectangle..."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare two rectangles and return the bigger or equal one

        Args:
            rect_1: first  rectangles
            rect_2: second rectangles

        Raises:
            TypeError: if rect_1 or rect_2 are not instances
        Returns:
            The biggest rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Create a square with equal width and height.

         Args:
             size: size of rectangles"""
        return cls(size, size)
