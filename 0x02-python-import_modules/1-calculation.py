#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    """print now"""
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, int(div(a, b))), end="\n")
