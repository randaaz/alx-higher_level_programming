#!/usr/bin/python3
"""Write a function that returns True if the object is an instance of,
    or if the object is an instanceof a class that inherited from,
    the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """
    Function to retrieve a list of attributes and methods of an object.

    Args:
        obj (object): The object to inspect.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
