#!/usr/bin/python3
"""define Square"""


class Square:
    """represent class square"""
    def __init__(self, size=0):
        """check for type"""

        if isinstance(size, int):

            """check for negative"""
            if size >= 0:
                self._Square__size = size
            else:
                print("size must be >= 0")
                raise ValueError
        else:
            print("size must be an integer")
            raise TypeError
