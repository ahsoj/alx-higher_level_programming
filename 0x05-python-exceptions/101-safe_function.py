#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        safe = fct(*args)
        return safe
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)


if __name__ == "__main__":
    safe_function()
