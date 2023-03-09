#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum = 0
    arg_list = sys.argv[1:]
    for arg in arg_list:
        sum += int(arg)
    print("{}".format(sum))
