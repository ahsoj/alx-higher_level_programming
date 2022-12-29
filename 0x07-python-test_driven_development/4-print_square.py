#!/usr/bin/python3


def print_square(size):
    """
        check for @size to the correct requirment
        and print matrix of @size result
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                j = "#"
                print(j, end="")
            print()
