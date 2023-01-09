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
