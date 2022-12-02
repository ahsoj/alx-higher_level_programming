#1/usr/bin/python3

import sys
nu = len(sys.argv)
mu = list(sys.argv)

from calculator_1 import add, sub, mul, div

if nu < 3:
    print("Usage: {} <a> <operator> <b>".format(mu[0]), end="\n")
elif mu[2] == "+":
    result = add(int(mu[1]), int(mu[3]))
    print("{} + {} = {}".format(mu[1], mu[3], result), end="\n")
elif mu[2] == "-":
    result == sub(int(mu[1]), int(mu[3]))
    print("{} - {} = {}".format(mu[1], mu[3], result), end="\n")
elif mu[2] == "*":
    result = mul(int(mu[1]), int(mu[3]))
    print("{} * {} = {}".format(mu[1], mu[3], result), end="\n")
elif mu[2] == "/":
    result = div(int(mu[1]), int(mu[3]))
    print("{} / {} = {}".format(mu[1], mu[3], result), end="\n")
else:
    print("Unknown operator. Available operators: +, -, * and /", end="\n")
