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

    def area(self):
        """This function returns the area of Rectangle"""
        return self.height * self.width
    
    def perimeter(self):
        """This function returns the perimeter of a Rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """This function returns the shape of the Rectangle as a string"""
        if self.width == 0 or self.height == 0:
                return ""
        else:
            rectangle = ["#" * self.width for _ in range(self.height)]
            return "\n".join(rectangle)

    def __repr__(self):
        """This function returns a representation string to recreate a new instance"""
        return f'Rectangle({self.width}, {self.height})'