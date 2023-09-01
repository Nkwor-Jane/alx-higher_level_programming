#!/usr/bin/python3
""" Function that finds a peak in a list of
unsorted integers"""
def find_peak(list_of_integers):
    left = 0
    right = len(list_of_integers)-1
    if list_of_integers is None or list_of_integers == []:
        return None
    while left<right-1:
        mid = (left + right)/2
        if list_of_integers[mid] > list_of_integers[mid+1] and list_of_integers[mid] > list_of_integers[mid-1]:
            return mid
        if list_of_integers[mid] < list_of_integers[mid +1]:
            left = mid+1
        else:
            right = mid - 1
    return left if list_of_integers[left] >= list_of_integers[right] else right
