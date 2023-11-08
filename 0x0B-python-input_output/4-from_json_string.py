#!/usr/bin/python3
import json

"""This module contain a function that return str rep of JSON"""
def from_json_string(my_str):
    """This function returns a Python data structure represented by a JSON string."""
    python_obj = json.loads(my_str)
    return python_obj
