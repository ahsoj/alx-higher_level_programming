#!/usr/bin/python3
"""Define `Base` class"""


class Base:
    """type: int -> private instance __nb_objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """retrive id in type of int"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
