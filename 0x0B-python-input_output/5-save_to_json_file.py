#!/usr/bin/python3
"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """write the json object to file"""
    with open(filename, 'w') as fp:
        json.dump(my_obj, fp)
