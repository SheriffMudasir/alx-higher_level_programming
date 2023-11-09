#!/usr/bin/python3
"""This module"""
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Validate width and height using integer_validator and """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
