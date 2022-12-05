#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print("{}".format(" ".join(map(str, i))))


if __name__ == "__main__":
    print_matrix_integer()
