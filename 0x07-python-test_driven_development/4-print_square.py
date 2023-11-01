#!/usr/bin/python3
"""This file contains one function that prints a square with the character #."""
def print_square(size):
    """
    This function prints a square with the character #.

    Args:
        a (int): size of square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    me = ["#" * size for _ in range(size)]
    me = "\n".join(me)
    print(me)