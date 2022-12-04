#!/usr/bin/pyton3

import sys
from calculator_1 import add, sub, mul, div

nu = len(sys.argv)
mu = list(sys.argv)
if len(mu) < 2:
    print("Usage: {} <a> <operator> <b>".format(mu[0]), end="\n")
else:
    a = int(mu[1])
    b = int(mu[3])

    def calcsec():
        if mu[2] == "+":
            res = add(a, b)
            print("{} + {} = {}".format(a, b, res), end="\n")
        elif mu[2] == "-":
            res = sub(a, b)
            print("{} - {} = {}".format(a, b, res), end="\n")
        elif mu[2] == "*":
            res = mul(a, b)
            print("{} * {} = {}".format(a, b, res), end="\n")
        elif mu[2] == "/":
            res = div(a, b)
            print("{} / {} = {}".format(a, b, res), end="\n")
        else:
            print("Unknown operator. Activable operators:", end=" ")
            print(" +, -, * and /")

    if __name__ == "__main__":
        calcsec()
