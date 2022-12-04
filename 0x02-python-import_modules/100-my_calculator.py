#!/usr/bin/pyton3
import sys
from sys import exit
from calculator_1 import add, sub, mul, div


def main():
    argc = sys.argv
    n = len(argc)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argc[1])
        b = int(argc[3])
        if argc[2] == "+":
            res = add(a, b)
            print("{} + {} = {}".format(a, b, res))
        elif argc[2] == "-":
            res = sub(a, b)
            print("{} - {} = {}".format(a, b, res))
        elif argc[2] == "*":
            res = mul(a, b)
            print("{} * {} = {}".format(a, b, res))
        elif argc[2] == "/":
            res = div(a, b)
            print("{} / {} = {}".format(a, b, res))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == '__main__':
    main()
