#!/usr/bin/python3
"""Module for class"""


class Student():
    """ Class that defines a Student"""

    def __init__(self, first_name, last_name, age):
        """ initializes student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """"retrieves a dictionaary representation of a Student"""
        return self.__dict__
