#!/usr/bin/python3
"""This module checks if an object is an instance of, or inherited from, a specified class"""
def is_kind_of_class(obj, a_class):
    """This function returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False"""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
