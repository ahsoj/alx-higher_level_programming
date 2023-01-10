#!/usr/bin/python3
""" `to_json_string` return JSON repersentation"""
import json


def to_json_string(my_obj):
    """serialize and return string/file"""
    return json.dumps(my_obj)  # option sort_keys=True
