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

    def update(self, *args, **kwargs):
        """This function adds a public method that assigns attributes using args and kwargs in this order:
        1st argument: id attribute
        2nd argument: size attribute
        3rd argument: x attribute
        4th argument: y attribute

        Parameters:
        - args: Variable positional number of arguments
        - kwargs: Variable number of keyword arguments
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
        
            def to_dictionary(self):
                """This function returns the dictionary representation of a Square"""
                return{
                    'id' : self.id,
                    'size' : self.size,
                    'x'   : self.x,
                    'y'   : self.y
            }
