#!/usr/bin/python3
"""This module checks if an object is exactly an instance of a specified class"""
def is_same_class(obj, a_class):
    """This function checks if an object is an instance of a specified class"""
    result = type(obj) is a_class
    return result
