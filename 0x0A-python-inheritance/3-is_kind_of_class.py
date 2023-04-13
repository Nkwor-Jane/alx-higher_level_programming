#!/usr/bin/python3
""" Module to check if object is an instance of the specifiied class."""


def is_kind_of_class(obj, a_class):
    """ function that returns True if the object is
    an instance of of if the object
    is an instance of a class inherited from
    the specified class; otherwise False"""
    result = isinstance(obj, a_class)
    if result:
        return True
    else:
        return False
