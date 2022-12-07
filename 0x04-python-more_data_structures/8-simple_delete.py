#!/usr/bin/pyton3


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        del(a_dictionary[key])
    else:
        pass
    return a_dictionary


if __name__ == "__main__":
    simple_delete()
