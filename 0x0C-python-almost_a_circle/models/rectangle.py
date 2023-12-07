#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of the Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """method for width."""
        return self.__width

    @width.setter
    def width(self, value):
        self.validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """method for height."""
        return self.__height

    @height.setter
    def height(self, value):
        self.validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        """method for x."""
        return self.__x

    @x.setter
    def x(self, value):
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """method for y."""
        return self.__y

    @y.setter
    def y(self, value):
        self.validation("y", value)
        self.__y = value

    def validation(self, name, value, e=True):
        """adding validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if e and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not e and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """The area value of the Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """ prints in stdout the Rectangle instance with
        the character #"""
        res = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(res, end='')

    def __str__(self):
        """informatin about rectangle."""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def u_arguments(self, id=None, width=None, height=None, x=None, y=None):
        """assigns an argument"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update argument"""
        if args:
            self.u_arguments(*args)
        if kwargs:
            self.u_arguments(**kwargs)

    def to_dictionary(self):
        '''dictionary representation'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
