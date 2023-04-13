#!/usr/bin/python3
"""Module to return dictionary description with simple DSA"""


def class_to_json(obj):
    """obj is an instance of a Class"""
    return(json.dumps(obj.__dict__))
