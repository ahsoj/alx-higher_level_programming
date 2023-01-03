#!/usr/bin/python3


def add_integer(a, b=98):
    """ check @a and @b for integer or not
        if it's true return int(value)
        else raise TypeError("Message)
    """
    if isinstance(a, (int, float)):
        pass
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        return int(a + b)
    raise TypeError("b must be an integer")
