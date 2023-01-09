#!/usr/bin/python3
"""Define ``BaseGeometry`` class"""


class BaseGeometry:
    """Define Public instance method"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method"""
        if not type(value) == int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
