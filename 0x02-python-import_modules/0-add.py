#!usr/bin/python3

if __name__ == "__main__":
    """ print now"""
    add = __import__("add_0").add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)), end="\n")
