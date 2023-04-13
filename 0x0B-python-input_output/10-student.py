#!/usr/bin/python3
"""Module for class"""


class Student():
    """ Class that defines a Student"""

    def __init__(self, first_name, last_name, age):
        """ initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """"retrieves a dictionaary representation of a Student"""
        if type(attrs) is list:
            attr_names = {}
            for k in self.__dict__:
                for k2 in attrs:
                    if k == k2:
                        attr_names[k] = self.__dict__[k]
            return attr_names
        else:
            return self.__dict__
