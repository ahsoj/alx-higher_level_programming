#!/usr/bin/python3
"""Define the class"""


class LockedClass:
    """
    define prevents the user from \
    dynamically creating new instance attributes
    """

    __slots__ = ['first_name']

