#!usr/bin/python3
from add_0 import add


def adds():
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)), end="\n")


if __name__ == "__main__":
    adds()
