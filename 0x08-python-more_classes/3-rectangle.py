#!/usr/bin/python3
""" Define Classes"""


class Rectangle:
    """define rectangle class"""

    def __init__(self, width=0, height=0):
        """Initilaize the rectangle class"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """return the value of self.__width"""
        return self.__width

    @width.setter
    def width(self, value):
        """check for @value to set to self.__width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the value of self.__height"""
        return self.__height

    @height.setter
    def height(self, value):
        """check for @value to set to self.__height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of width * height"""
        return self.width * self.height

    def perimeter(self):
        """return perimeter of (width + height) * 2"""
        if self.__width == 0 == self.__height:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """return character of ``#`` by(width * height) \
        scale if width or height is gt 0 else return empty string"""
        if self.__width == 0 == self.__height:
            return ""
        return (("#" * self.__width + "\n") * self.__height).rstrip()
