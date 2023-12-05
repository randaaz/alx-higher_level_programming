#!/usr/bin/python3
""""a class Student that defines a student"""


class Student:
    """"a class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """defines a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json  dictionary"""
        try:
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        new_d = dict()
        for k, v in self.__dict__.items():
            if k in attrs:
                new_d[k] = v
        return new_d

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v
