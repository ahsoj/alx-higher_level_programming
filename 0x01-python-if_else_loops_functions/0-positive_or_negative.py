#!/usr/bin/python3
import random
number = random.randint(-10, 10)

def spire():
    if number < 0:
        print("{:d} is negative".format(number))
    elif number == 0:
        print("{:d} is zero".format(number))
    elif number > 0:
        print("{:d} is positive".format(number))
if __name__ == "__main__":
    spire()
