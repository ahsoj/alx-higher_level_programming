#!/usr/bin/python3
"""write a `read_file` function for reading file content"""


def read_file(filename=""):
    """read content from a given file"""
    with open(filename, 'r', encoding='UTF8') as fp:
        print(fp.read())
