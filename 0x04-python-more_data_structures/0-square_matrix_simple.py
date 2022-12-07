#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    allIn = ([list(map(lambda x: x * x, i)) for i in matrix])
    return allIn


if __name__ == "__main__":
    square_matrix_simple()
