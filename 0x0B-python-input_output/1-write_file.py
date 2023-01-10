#!/usr/bin/python3
"""write a `write_file` function to write file content"""


def write_file(filename="", text=""):
    """write af ile and count characters"""
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(text)
    return len(open(filename).read())
