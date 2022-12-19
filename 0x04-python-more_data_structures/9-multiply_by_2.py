#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    return ({i: a_dictionary[i] * 2 for i in a_dictionary})


if __name__ == "__main__":
    multiply_by_2()
