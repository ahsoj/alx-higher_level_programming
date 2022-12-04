#!usr/bin/python3
from add_0 import add


def adds():
    a = 1
    b = 2
    print("{} + {} = {}".format(str(a), str(b), str(add(a, b))))


if __name__ == "__main__":
    adds()
