#!/usr/bin/python3


def search_replace(my_list, search, replace):
    allIn = my_list[:]
    for i in range(len(allIn)):
        if allIn[i] == search:
            allIn[i] = replace
    return allIn


if __name__ == "__main__":
    search_replace()
