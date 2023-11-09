#!/usr/bin/python3
"""This module checks for class inheritance"""


def inherits_from(obj, a_class):
    """This function returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False"""
    return issubclass(type(obj), a_class)