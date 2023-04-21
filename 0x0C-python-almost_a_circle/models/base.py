#!/usr/bin/python3
""" Module for class Base"""
import json


class Base():
    """ Base class """
    """ private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize public instance attibute and reassign id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to file"""
        if list_objs is None:
            return []
        filename = cls.__name__ + ".json"
        json_str = []
        for i in list_objs:
            json_str.append(i.to_dictionary())
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(json_str))

    @staticmethod
    def from_json_string(json_string):
        """"returns list of json string representation json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instances with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ == "Sqaure":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy
