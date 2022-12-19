#!/usr/bin/python3


def safe_print_integer_err(value):
    set = False
    try:
        if isinstance(value, int):
            print(value)
            set = True
        else:
            raise TypeError
        return set
    except TypeError:
        print("Exception: Unknown format code 'd' for object of type 'str'")


if __name__ == "__main__":
    safe_print_integer_err()
