#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) <= 0:
        pass
    else:
        my_list.sort()
        return my_list[-1]


if __name__ == "__main__":
    max_integer()
