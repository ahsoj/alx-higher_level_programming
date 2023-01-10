#!/usr/bin/python3
""" `to_json_string` return JSON repersentation"""
import json


def from_json_string(my_str):
    """serialize and return string/file"""
    return json.loads(my_str)
