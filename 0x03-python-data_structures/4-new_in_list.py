#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    my_list_copy = []
    for i in range(len(my_list)):
        my_list_copy.append(my_list[i])
    if idx < 0:
        return my_list_copy
    elif idx >= len(my_list):
        return my_list_copy
    else:
        my_list_copy[idx] = element
        return my_list_copy


if __name__ == "__main__":
    new_in_list()
