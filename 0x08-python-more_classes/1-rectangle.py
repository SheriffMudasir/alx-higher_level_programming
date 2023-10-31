#!/usr/bin/python3
"""Define a class Rectangle"""
class Rectangle:
    """This class represent a Rectangle"""
    def __init__(self, width = 0, height = 0):
        """
        Initialize a Rectangle.

        Args:
        width (int): The width of the Rectangle  (default is 0).
        height (int): The height of the Rectangle  (default is 0).
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Getter to retrieve the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Setter to set the value of the width and check type validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= zero")
        self.__width = value

    @property
    def height(self):
        """Getter to retrieve the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Setter to set the value of the height and check type validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= zero")
        self.__height = value
    