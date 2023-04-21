#!/usr/bin/python3
""" Module Sqaure inherits from Rectangle"""

from rectangle import Rectangle


class Square(Rectangle):
    """ Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize class with private instance attributes,
        id, x, y"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """gets private instance attribute size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """sets private instance attribute size assigned
        with the value of width and height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """override __str__ method with [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square]({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """update the Square class by adding public method
        update with **kwargs attribute to
        assign key/value srguments to attributes"""
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
