#!/usr/bin/python3
import json

""""This module contain one function that convert json to obj"""
def load_from_json_file(filename):
    """This function creates an object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        loaded_object = json.load(file)
    return loaded_object

         