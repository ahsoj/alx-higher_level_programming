#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    last = number % 10
    if number == 1:
        number *= -1
    print("{:d}".format(last), end="")
    return last
if __name__ == "__main__":
    print_last_digit()
