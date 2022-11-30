#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if j >= ord('a') and j <= ord('z'):
            j = chr(j - 32)
        print("{}".format(i), end="")
    print()

if __name__ == "__main__":
    uppercase()

