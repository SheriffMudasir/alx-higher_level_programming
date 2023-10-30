#!/usr/bin/python3
"""Define a class Square"""
class Square:
    """This class Square has the size, position, my_print function"""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.

        Args:
        size (int): The size of the new square (default is 0).
        position (tuple): The position of the square (default is (0, 0)).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with type and value validation."""
        if (not isinstance(value, tuple) or
    len(value) != 2 or
    not all(isinstance(i, int) and i >= 0 for i in value)):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square with '#' characters and position control."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
