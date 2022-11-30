#!/usr/bin/python3
de uppercase(str):
    for i in str:
        j = ord(i)
        if j > ord("a") and j < ord("z"):
            j = (chr(j - 32)
        else:
            j = (chr(j))
        print(j, end="")
    print()
if __name__ == "__main__":
    uppercase()
