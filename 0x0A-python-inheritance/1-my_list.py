#!/usr/bin/python3
""" Module on inheritance"""


class MyList(list):
    """ class that inherits from list"""
    def print_sorted(self):
        """public instance method to sort list"""
        print(sorted(self))
