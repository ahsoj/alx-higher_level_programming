#!/usr/bin/python3
""" class `Square` that inherits from `Rectangle`"""
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                if a == 1:
                    self.size = arg
                if a == 2:
                    self.x = arg
                if a == 3:
                    self.y = arg
                a += 1


        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
        
    def to_dictionary(self):
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y,
        }


    def __str__(self) -> str:
        """[Square] (<id>) <x>/<y> - <size>"""
        rect = "[Square] ({}) {}/{} - {}"
        return rect.format(self.id, self.x, self.y, self.size)
