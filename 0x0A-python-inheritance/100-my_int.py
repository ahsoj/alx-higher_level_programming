#!/usr/bin/python3
"""Define `MyInt` class"""


class MyInt(int):
    """Use type->int inherit"""

    def __eq__(self, other):
        """invert == to !="""
        return self.real != other

    def __ne__(self, other):
        """invert != to =="""
        return self.real == other
