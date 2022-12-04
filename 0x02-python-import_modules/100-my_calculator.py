#1/usr/bin/pyton3

import sys
nu = len(sys.argv)
mu = list(sys.argv)

a = int(mu[1])
b = int(mu[3])

from calculator_1 import add, sub, mul, div

if nu < 3:
    print("Usage: {} <a> <operator> <b>".format(mu[0]), end="\n")
elif mu[2] == "+":
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
    print("Unknown operator. Activable operators: +, -, * and / ", end="\n")
