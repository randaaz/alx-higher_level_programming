#!/usr/bin/python3
""" Adds two integers Module"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
