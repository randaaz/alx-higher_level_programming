#!/usr/bin/python3
"""Base class module"""
from json import dumps, loads


class Base:
    """The Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new instance of the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ JSON string representation"""
        if json_string is None or not json_string:
            return []
        else:
            return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as fi:
            fi.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        """an instance with all attributes already set"""
        from rectangle import Rectangle
        from square import Square
        if cls is Rectangle:
            new_o = Rectangle(1, 1)
        elif cls is Square:
            new_o = Square(1)
        else:
            new_o = None
        new_o.update(**dictionary)
        return new_o

    @classmethod
    def load_from_file(cls):
        """list of instances"""
        from os import path
        json_fi = "{}.json".format(cls.__name__)
        if not path.isfile(json_fi):
            return []
        with open(json_fi, "r", encoding="utf-8") as fi:
            return [cls.create(**c) for c in cls.from_json_string(fi.read())]
