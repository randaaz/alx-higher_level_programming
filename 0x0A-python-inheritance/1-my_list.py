#!/usr/bin/python3
"""class MyList that inherits class list"""


class MyList(list):
    """A custom list class with an additional method for sorted printing."""
    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
