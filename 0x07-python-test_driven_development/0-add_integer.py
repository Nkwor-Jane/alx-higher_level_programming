#!/usr/bin/python3
def add_integer(a, b=98):
    """"Function that addds two integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must ba an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
