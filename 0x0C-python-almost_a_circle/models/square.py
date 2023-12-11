#!/usr/bin/python3
"""souare class module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """souare class"""

    def __init__(self, size, x=0, y=0, id=None):
        """informatin."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """informatin about souare"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """"method for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def u_arguments(self, id=None, size=None, x=None, y=None):
        """assigns an argument"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update argument"""
        if args:
            self.u_arguments(*args)
        elif kwargs:
            self.u_arguments(**kwargs)

    def to_dictionary(self):
        """representation"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
