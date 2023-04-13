#!/usr/bin/python3
""" Module to check if object is an instance of the specifiied class."""


def is_same_class(obj, a_class):
    """ function that returns True if the object is exactly
    an instance of the specified class; otherwise False"""
    result = type(obj)
    if result is a_class:
        return True
    else:
        return False
