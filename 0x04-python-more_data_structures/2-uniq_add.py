#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_list = []
    result = 0
    for q in my_list:
        if q not in unique_list:
            unique_list.append(q)
    for q  in unique_list:
        result += q
    return result


if __name__ == "__main__":
    uniq_add()
