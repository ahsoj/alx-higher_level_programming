#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    set = False
    try:
        if isinstance(value, int):
            print(value)
            set = True
        else:
            sys.stderr.write("Exception: Unknown format code 'd' for object of type 'str'")
        return set
    except TypeError:
        raise


if __name__ == "__main__":
    safe_print_integer_err()
