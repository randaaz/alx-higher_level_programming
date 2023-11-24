#!/usr/bin/python3
"""print_square method."""


def print_square(size):
    """
    Print a square of '#' characters with the given size.

    Parameters:
        size (int): The size of the square. Must be a non-negative integer.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is less than 0.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
