#!/usr/bin/pyton3


def main(argv):
    n = len(argv)
    idx = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    if n != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
    else:
        a = int(argv[1])
        b = int(argv[3])
        c = argv[2]
        if c not in '+-*/':
            print('Unknown operator. Available operators: +, -, * and /')

        res = idx[c](a, b)
        print('{:d} {:s} {:d} = {:d}'.format(a, c, b, res))


if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div
    main(argv)
