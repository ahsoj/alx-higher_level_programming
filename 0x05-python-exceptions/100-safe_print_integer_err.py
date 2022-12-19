#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    set = False
    try:
        
        print("{:d}".format(value))
        return True
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False


if __name__ == "__main__":
    safe_print_integer_err()
