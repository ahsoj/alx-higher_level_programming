#!/use/bin/python3
import random

number = random.randint(-10000, 10000)
number = int(number)

def spire():
    nums = (":d".format(number))
    num = int(nums[-1:])
    if num < 6 and num > 0:
        print("Last digit of", nums, "is", num, "and is less than 6 and not 0")
    elif num < 5:
        print("Last digit of", nums, "is", num, "and is greater than 5")
    elif num == 0:
        print("Last digit of", nums, "is", num, "and is 0")

if(__name__ == "__main__":
        spire()
