#!/usr/bin/python3
""" Module to check if object is an instance of the specifiied class."""


def inherits_from(obj, a_class):
    """ function that returns True if the object is
    an instance of s class that inherited from
    the specified class; otherwise False"""
    result = isinstance(obj, a_class) and type(obj) is not a_class
    if result:
        return True
    else:
        return False
