#!/usr/bin/python3
"""Define class `Rectangle` that inherits from `Base` """
from models.base import Base


class Rectangle(Base):
    """retrive constractor for this class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """assign all in constructor to proper way"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get and property function"""
        return self.__width

    @width.setter
    def width(self, val):
        """setter for `width`"""
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise TypeError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        """get and property function"""
        return self.__height

    @height.setter
    def height(self, val):
        """setter for `height`"""
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise TypeError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        """get and property function"""
        return self.__x

    @x.setter
    def x(self, val):
        """setter for `x`"""
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise TypeError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """get and property function"""
        return self.__y

    @y.setter
    def y(self, val):
        """setter for `y`"""
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise TypeError("y must be >= 0")
        else:
            self.__y = val

    def area(self):
        """returns the area value of the `Rectangle` instance."""
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle \
            instance with the character # """
        [print("") for y in range(self.y)]
        for x_a in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
    
    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self) -> str:
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        rect = "[Rectangle] ({}) {}/{} - {}/{}"
        return rect.format(self.id, self.x, self.y, self.width, self.height)