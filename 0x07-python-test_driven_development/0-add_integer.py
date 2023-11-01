#!/usr/bin/python3
"""This file contains one function for adding integer"""
def add_integer(a, b=98):
    """
    This function add two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number (default is 98).

    Returns:
        int: The sum of a and b as an integer.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
