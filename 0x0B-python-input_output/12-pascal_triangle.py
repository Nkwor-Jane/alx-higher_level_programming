#!/usr/bin/python3
""" Module to return list of integers representing
Pascal's triangle n"""


def pascal_triangle(n):
    """function to return list of inteers"""
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):
        return (' '*(n-i), end='')
