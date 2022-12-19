#!/usr/bin/python3


def safe_print_division(a, b):
    set = 0
    try:
        set = a / b
    except ZeroDivisionError:
        set = None
    finally:
        print("Inside result: {}".format(set))
        return set


if __name__ == "__main__":
    safe_print_division()
