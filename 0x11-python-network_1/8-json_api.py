#!/usr/bin/python3
"""
     Python script that takes in a \
     letter and sends a POST request
"""
import requests


def main(_arg):
    """
        sends a POST request to http://0.0.0.0:5000/search_user \
                with the letter as a parameter.
    """
    payload = {"q": _arg}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    from sys import argv
    main("" if len(argv) == 1 else argv[1])
