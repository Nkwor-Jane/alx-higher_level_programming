#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            ltou = ord(str[i]) + ord('A') - ord('a')
        else:
            ltou = ord(str[i])
        print("{}".format(chr(ltou)), end='')
    print()
