#!/usr/bin/python3
class Square:
        """Define a class Square"""

        def __init__(self, size=0):
            """
            Initialize a new square.

            Args:
            size (int): The size of the new square (default is 0).
            """
            self.size = size

        @property
        def size(self):
            """Retrieve the size of the square."""
            return self.__size

        @size.setter
        def size(self, value):
            """Set the size of the square with type and value validation."""
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """
            Calculate and return the area of the square.

            Returns:
            int: The area of the square.
            """
            return self.__size * self.__size
