#!/usr/bin/python3
"""Base class module"""
from json import dumps, loads
import csv


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
        from models.rectangle import Rectangle
        from models.square import Square
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes and deserializes in CSV"""
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """serializes and deserializes in CSV"""
        from models.rectangle import Rectangle
        from models.square import Square
        res = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as file:
            reader = csv.reader(file)
            for w in reader:
                w = [int(i) for i in w]
                if cls is Rectangle:
                    dec = {"id": w[0], "width": w[1], "height": w[2],
                           "x": w[3], "y": w[4]}
                else:
                    dec = {"id": w[0], "size": w[1],
                           "x": w[2], "y": w[3]}
                res.append(cls.create(**dec))
        return res

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for j in list_rectangles + list_squares:
            tut = turtle.Turtle()
            tut.color((randrange(255), randrange(255), randrange(255)))
            tut.pensize(1)
            tut.penup()
            tut.pendown()
            tut.setpos((j.x + tut.pos()[0], j.y - tut.pos()[1]))
            tut.pensize(10)
            tut.forward(j.width)
            tut.left(90)
            tut.forward(j.height)
            tut.left(90)
            tut.forward(j.width)
            tut.left(90)
            tut.forward(j.height)
            tut.left(90)
            tut.end_fill()

        time.sleep(5)
