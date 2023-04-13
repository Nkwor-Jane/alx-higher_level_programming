#!/usr/bin/python3
""" function to read a text file and print to stdout"""


def read_file(filename=""):
    """ reads text file and prints it to stdout."""
    with open(filename, 'r') as f:
        print(f.read(), end="")
