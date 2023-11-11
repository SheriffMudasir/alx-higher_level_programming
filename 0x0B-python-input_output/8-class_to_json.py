#!/usr/bin/python3
"""This module contain one function that returns a data structure"""
def class_to_json(obj):
    """This function returns the dictionary description of a serializable object."""
    obj_dict = obj.__dict__
    
    for key, value in obj_dict.items():
        if isinstance(value, list):
            obj_dict[key] = [item for item in value if isinstance(
                item, (str, int, bool, list, dict))]
        elif isinstance(value, dict):
            obj_dict[key] = {k: v for k, v in value.items(
            ) if isinstance(v, (str, int, bool, list, dict))}
        elif not isinstance(value, (str, int, bool, list, dict)):
            obj_dict[key] = str(value)

    return obj_dict
