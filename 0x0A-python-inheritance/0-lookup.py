#!/usr/bin/python3
"""Define lookup function"""


def lookup(obj):
    """
    returns the list of available \
    attributes and methods of an object
    """
    return list(dir(obj))
