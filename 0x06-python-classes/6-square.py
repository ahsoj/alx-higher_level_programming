
class Square:
    """represent class square"""
    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        if isinstance(position, tuple):
            self._Square__position = position
        else:
            print("position must be a tuple of 2 positive integers", end="")
            """raise error message"""
            raise TypeError
    
    @property
    def position(self):
        return self._Square__position

    @position.setter
    def position(self, value):
        if len(value) >= 2 and value > 0:
            self._Square__position = value
        print("position must be a tuple of 2 positive integers")
        raise TypeError
    
    @property
    def size(self):
        return self._Square__size
    
    def area(self):
        """get and calculate area"""
        print(self._Square__size * self._Square__size)
    
    def my_print(self):
        if self._Square__size == 0:
            print("\n")
        for i in range(self._Square__size):
            for j in range(self._Square__size):
                print("#", end="")
            print()
    
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
    