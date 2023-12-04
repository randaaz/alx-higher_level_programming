#!/usr/bin/python3
"""function that returns True if the object is exactly an instance
    of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """
    Function to retrieve a list of attributes and methods of an object.

    Args:
        obj (object): The object to inspect.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
