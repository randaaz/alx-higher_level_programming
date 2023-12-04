#!/usr/bin/python3
"""Custom integer class with modified equality and inequality comparisons."""


class MyInt(int):
    """Inheritance class"""
    def __new__(cls, *args, **kwargs):
        """Overrides the creation of a new instance."""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """ Overrides the equality comparison."""
        return int(self) != other

    def __ne__(self, other):
        """ Overrides the inequality comparison."""
        return int(self) == other
