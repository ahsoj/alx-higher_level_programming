#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    chack for {first_name and last_name} == str
    and print the result
    otherwise raise TypeError: "message"
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    Fn = first_name
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    Ln = last_name
    print(f"My name is {Fn} {Ln}")
