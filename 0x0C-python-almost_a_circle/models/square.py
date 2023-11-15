#!/usr/bin/python3
"""This module is the implementation of the square module which inherits from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a square class that inherits from most of his own music
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size property."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size property.
        Parameter
        -value (int): The new value of height and width

        Raises:
        -TypeError: if the value is not an int 
        -ValueError: if the value is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be of integer value")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides the default string representation of the object.

        Returns:
        - str: A formatted string representing the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
