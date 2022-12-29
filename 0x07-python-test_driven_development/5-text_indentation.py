#!/usr/bin/python3


def text_indentation(text):
    """
        check for @text is string or not
        if !text raise TypeError: Message
        else print(text)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, f"{char}\n\n")
    for ln in text.splitlines():
        print(ln.lstrip(' '))
