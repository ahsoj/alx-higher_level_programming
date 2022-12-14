#!/usr/bin/python3
"""define Square"""


class Square:
    """represent class square"""
    def __init__(self, size=0):
        self._Square__size = size

    @property
    def size(self):
        return self._Square__size

    def area(self):
        """get and calculate area"""
        return (self._Square__size * self._Square__size)

    @size.setter
    def size(self, value):
        """setter a value on size"""
        if isinstance(value, int):
            """check for data type"""

            if value >= 0:
                """check for negative"""
                self._Square__size = value
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
