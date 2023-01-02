#!/usr/bin/python3
""" Define Classes"""


class Rectangle:
    """define rectangle class"""
    all = []

    def __init__(self, width=0, height=0):
        """Initilaize the rectangle class"""
        self.__height = height
        self.__width = width
        Rectangle.all.append(self)

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
