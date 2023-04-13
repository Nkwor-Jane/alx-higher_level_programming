#!/usr/bin/python3
"""Module on Inheritance---- Used Imports ---- Square class
inherits from Rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle class... Super!"""

    def __init__(self, size):
        """initialize Square public instance"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """return area of square"""
        return (self.__size * self.__size)
