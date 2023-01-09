#!/usr/bin/python3
"""Use ``Rectangle` in `Square` class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define `Rectangle` class"""

    def __init__(self, size):
        """Instantiation square with `size` """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """print square of size"""
        return (self.__size * self.__size)
