#!/usr/bin/python3
"""create Rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets width instance attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets width instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets height instance attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets height instance attribute"""
        if type(value) is not int:
            raise TypeError("height must be integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return area of rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """"return perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """print rectanlg with the character'#'"""
        string_rep = ""
        if self.width == 0 or self.height == 0:
            return (string_rep)
        for x in range(self.height):
            for y in range(self.width):
                string_rep += "#"
            string_rep += "\n"
        string_rep = string_rep[:-1]
        return (string_rep)
