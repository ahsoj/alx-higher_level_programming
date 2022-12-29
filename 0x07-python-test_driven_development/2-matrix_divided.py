#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
        first check if @matrix is listoflist of integer or float,
        check row of the @matrix must have the same size
        check @div for != 0 if 0 raise an Error Message
        if pass check function return matrix of list.
    """

    if all(isinstance(s, list) for s in matrix):
        if len(matrix[0]) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
        elif not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        for i in matrix:
            if all(isinstance(s, (int, float)) for s in i):
                if div != 0:
                    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
                raise ZeroDivisionError("division by zero")
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
