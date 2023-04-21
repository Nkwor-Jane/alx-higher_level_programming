#!/usr/bin/python3
"""13-main"""
from square import Square

if __name__ == "__main__":

    s1 = Square(10,2,1)
    print(s1)
    s1_dict = s1.to_dictionary()
    print(s1_dict)
    print(type(s1_dict))

    s2 = Square(1,1)
    print(s2)
    s2.update(**s1_dict)
    print(s2)
    print(s1 == s2)
