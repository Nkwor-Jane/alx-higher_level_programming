#!/usr/bin/python3
""" Function that finds a peak in a list of
unsorted integers"""
def find_peak(list_of_integers):
    low = 0
    high = len(list_of_integers)-1
    while low<high:
        mid = low + (high - low+1)//2
        if (mid-1>=0 and list_of_integers[mid-1]<=list_of_integers[mid]):
            low = mid
        else:
            high = mid - 1
    return list_of_integers[low+1]
