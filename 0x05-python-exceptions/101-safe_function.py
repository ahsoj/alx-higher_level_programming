#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    safe = ""
    try:
        safe = fct(*args)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    else:
        return safe


if __name__ == "__main__":
    safe_function()
