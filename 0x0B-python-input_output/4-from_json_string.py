#!/usr/bin/python3
"""This module contain a function that return str rep of JSON"""
import json

def from_json_string(my_str):
    """This function returns a Python data structure represented by a JSON string."""
    python_obj = json.loads(my_str)
    return python_obj
