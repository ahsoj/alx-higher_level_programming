#1/usr/bin/python3

if __name__ == "__main__":
    """print  now"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "_":
            print(name)