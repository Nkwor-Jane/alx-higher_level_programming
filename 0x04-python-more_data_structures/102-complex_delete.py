#!/usr/bin/python3
def complex_delete(a_dictionary, key=""):
    specifics = []
    for k, v in a_dictionary.items():
        if k is v:
            specifics.append(key)
    for x in specifics:
        del a_dictionary[x]
    return (a_dictionary)
