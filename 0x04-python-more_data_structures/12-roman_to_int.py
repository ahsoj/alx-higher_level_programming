#!/usr/bin/python3


def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    roman_back = list(reversed(list(roman_string)))
    value = 0
    right_val = roman_dict[roman_back[0]]
    for numeral in roman_back:
        left_val = roman_dict[numeral]
        if left_val < right_val:
           value -= left_val
        else:
            value += left_val
        right_val = left_val
    return value


if __name__ == "__main__":
    roman_to_int()
