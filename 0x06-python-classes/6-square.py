#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square."""
        self._Square__size = size
        self._Square__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self._Square__size)

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self._Square__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        self._Square__position = value

    def area(self):
        """Return the current area of the square."""
        return (self._Square__size * self._Square__size)

    def my_print(self):
        """Print the square with the # character."""
        if self._Square__size == 0:
            print("")
            return
        [print("") for i in range(0, self._Square__position[1])]
        for i in range(0, self._Square__size):
            [print(" ", end="") for j in range(0, self._Square__position[0])]
            [print("#", end="") for k in range(0, self._Square__size)]
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
