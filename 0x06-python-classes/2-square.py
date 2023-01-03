#!/usr/bin/python3
"""define Square"""


class Square:
    """represent class square"""
    def __init__(self, size=0):

        if isinstance(size, int):
            """check for data type"""

            if size >= 0:
                """check for negative"""
                self._Square__size = size
            else:
                """if not true"""
                print("size must be >= 0", end="")
                """raise error message"""
                raise ValueError
        else:
            """if not true"""
            print("size must be an integer", end="")
            """raise error message"""
            raise TypeError
