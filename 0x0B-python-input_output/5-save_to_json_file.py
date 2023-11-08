#!/usr/bin/python3
import json
"""This module"""

def save_to_json_file(my_obj, filename):
    """This function saves an object to a text file in JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
