#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_new_tuple = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = tuple_a + a_new_tuple
    if len(tuple_b) < 2:
        tuple_b = tuple_b + a_new_tuple
    first_value = tuple_a[0] + tuple_b[0]
    second_value = tuple_a[1] + tuple_b[1]
    newer_tuple = (first_value, second_value)
    return(newer_tuple)
