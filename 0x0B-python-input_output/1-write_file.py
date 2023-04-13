#!/usr/bin/python3
""" function that writes a string to a textfile and
returns number of characters needed"""


def write_file(filename="", text=""):
    """ write text file and returns number oc characters."""
    with open(filename, 'w') as f:
        return f.write(text)
