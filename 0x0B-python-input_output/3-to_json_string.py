#!/usr/bin/python3
"""Function that returns JSON representation of an object"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object"""
    return json.dumps(my_obj)
