#!/usr/bin/python3
"""add attribute"""


def add_attribute(o, a, v):
    """add attribute"""
    if not hasattr(o, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(o, a, v)
