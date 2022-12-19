#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    res = []
    for i in set_1:
        if i in set_2:
            pass
        else:
            res.append(i)
    for i in set_2:
        if i in set_1:
            pass
        else:
            res.append(i)
    return res


if __name__ == "__main__":
    only_diff_elements()
