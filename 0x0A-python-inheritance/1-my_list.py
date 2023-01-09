#!/usr/bin/python3
"""Define MyList class"""


class MyList(list):
    """ inherit from list """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
