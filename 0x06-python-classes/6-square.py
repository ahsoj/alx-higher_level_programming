#!/usr/bin/python3
"""define class Square"""


class Square:
    """represent class square"""
    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        self._Square__position = position

    @property
    def position(self):
        """Private instance attribute to retrive it"""
        return self._Square__position

    @position.setter
    def position(self, value):
        """property setter"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        self.__position = value

    @property
    def size(self):
        """Private instance attribute to retrive it"""
        return self._Square__size

    def area(self):
        """get and calculate area"""
        print(self._Square__size * self._Square__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

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
