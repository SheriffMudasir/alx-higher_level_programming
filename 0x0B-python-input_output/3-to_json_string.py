#!/usr/bin/python3
"""This module contain a function that return JSON rep"""
import json
def to_json_string(my_obj):
    """This function returns the JSON representation of an object (string):"""
    json_string = json.dumps(my_obj)
    return json_string


