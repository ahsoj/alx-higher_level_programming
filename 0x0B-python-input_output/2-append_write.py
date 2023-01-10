#!/usr/bin/python3
"""write a `write_file` function to write file content"""


def append_write(filename="", text=""):
    """write af ile and count characters"""
    with open(filename, 'a', encoding='UTF8') as fp:
        fp.write(text)
    return len(open(filename).readline())