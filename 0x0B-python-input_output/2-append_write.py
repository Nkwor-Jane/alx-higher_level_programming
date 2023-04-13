#!/usr/bin/python3
""" function that append a string to a textfile and
returns number of characters needed"""


def append_write(filename="", text=""):
    """ append a string and returns number of characters."""
    with open(filename, 'a+') as f:
        return f.write(text)
