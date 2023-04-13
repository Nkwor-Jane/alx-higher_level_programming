#!/usr/bin/python3
""" Module that returnss list of available attributes and methods. """


def lookup(obj):
    """function that returns list of available attributes and methods"""
    return(dir(obj))
