#!/usr/bin/python3
"""create Rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        """return string representation of rectangle
        to recreate new instance"""
        repr_str = "Rectangle(%s, %s)" % (self.width, self.height)
        return (repr_str)

    def __del__(self):
        """prints message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not rect_1:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not rect_2:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)
