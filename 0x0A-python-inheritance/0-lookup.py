#!/usr/bin/python3
"""function that returns the list of available attributes and methods"""


def lookup(obj):
    """
    Function to retrieve a list of attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A sorted list containing the names of attributes and methods.
    """
    return (dir(obj))
