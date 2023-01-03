#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    set = 0
    try:
        for i in my_list[:x]:
            if isinstance(i, (int)):
                print("{:d}".format(i), end="")
                set += 1
        print()
        return set
    except IndexError as msg:
        print("{}".format(msg))


if __name__ == "__main__":
    safe_print_list_integers()
