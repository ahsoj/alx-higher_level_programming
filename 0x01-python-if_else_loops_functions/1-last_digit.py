#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
if number < 0:
    i = -1 * (- number % 10)
else:
    i = number % 10

if i > 5:
    print("Last digit of {:d} is {:d} and is greater than 5 and not 0".format(number, i)
elif i == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, i))
elif i < 6 and i != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(number, i), end= "\n")
