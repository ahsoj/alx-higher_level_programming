#!/usr/bin/python3
""" Define Classes"""


class Rectangle:
    """define rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initilaize the rectangle class"""
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                if rect_1.area() > rect_2.area():
                    return rect_1
                return rect_2
            raise TypeError("rect_2 must be an instance of Rectangle")
        raise TypeError("rect_1 must be an instance of Rectangle")

    def __str__(self):
        """Return the Rectangle."""
        if self.__width == 0 == self.__height:
            return ""
        return ((str(self.print_symbol) * self.__width + "\n") * self.__height).strip()

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle({}, {})"
        return rect.format(self.__width, self.__height).strip()

    def __del__(self):
        """Bye rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
