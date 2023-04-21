#!/usr/bin/python3
""" Module Rectangle inherits from Base"""

from base import Base


class Rectangle(Base):
    """ Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize class with private instance attributes,
        width, height, x, y"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """gets private instance attribute x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """sets private instance attibute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """gets private instance attribute y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """sets private instance attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """public method area-- to find area of rectangle"""
        return (self.width * self.height)

    def display(self):
        """public method that prints to stdout the Rectangle
        with the character #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print("", end='')
            for j in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """override __str__ method with [Rectangle]
        (<id>) <x>/<y> - <width>/<height>"""
        return ("[{}]({}) {}/{} - {}/{}"
                .format(self.__class__.__name__,
                        self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """update the Rectangle class by adding public method
        update with **kwargs attribute to assign key/value
        arguments to attributes"""
        if args is not None and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
        elif kwargs is not None and len(kwargs) != 0:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dictionary representation of a Rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
