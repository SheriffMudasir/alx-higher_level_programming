#!/usr/bin/python3
"""Define a class Square"""
class Square:
    """This class Square has the constructor and an additional def area which return the area of the square"""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size
