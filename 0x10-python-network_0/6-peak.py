#!/usr/bin/python3
"""Technical interview preparation"""


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers."""

    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    mid = len(list_of_integers) // 2
    if (list_of_integers[mid] > list_of_integers[mid - 1] and 
        list_of_integers[mid] > list_of_integers[mid + 1]):
        return list_of_integers[mid]
    elif list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
