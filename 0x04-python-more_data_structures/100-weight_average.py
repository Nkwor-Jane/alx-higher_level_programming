#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    av = 0
    total = 0
    for x, y in my_list:
        av += (x * y)
        total += y
    return (av /total)
