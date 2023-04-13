#!/usr/bin/python3
""" Module on Inheritance--- could have used import. Oh Well!"""


class BaseGeometry:
    """BaseGeometry class - to raise exception
    and validate integer in public instance method"""

    def area(self):
        """raises exception that area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
