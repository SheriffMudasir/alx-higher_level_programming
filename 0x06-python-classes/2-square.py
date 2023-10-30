#!/usr/bin/python3
"""Define a class Square"""
class Square:
    """This class represent a Square"""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of the new square. It should be a non-negative integer.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
