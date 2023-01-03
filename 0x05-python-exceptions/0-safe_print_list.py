#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    set = 0
    try:
        for i in my_list[:x]:
            print("{}".format(i), end="")
            set += 1
        print()
        return set
    except ValueError:
        pass


if __name__ == "__main__":
    set_print_list()
