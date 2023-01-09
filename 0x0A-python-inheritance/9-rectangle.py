#!/usr/bin/python3
"""Use ``BaseGeometry` in `Rectangle` class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define `Rectangle` class"""

    def __init__(self, width, height):
        """Instantiation with ` `width` and `height` `"""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """print area of width * height"""
        return self.__width * self.__height

    def __str__(self):
        """return string formated"""
        return f"[Rectangle] {self.__width}/{self.__height}"
