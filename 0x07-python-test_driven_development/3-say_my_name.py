#!/usr/bin/python3
""" say_my_name method"""


def say_my_name(first_name, last_name=""):
    """
    Print a formatted message stating a person's name.

    Parameters:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person.

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
