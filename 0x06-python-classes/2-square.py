#!/usr/bin/python3
"""define Square"""


class Square:
    """represent class square"""
    def __init__(self, size=0):
        """check for data type"""

        if isinstance(size, int):

            """check for negative"""
            if size >= 0:
                self._Square__size = size
            """if not true"""
            else:
                print("size must be >= 0")
                """raise error message"""
                raise ValueError
        """if not true"""
        else:
            print("size must be an integer")
            """raise error message"""
            raise TypeError
