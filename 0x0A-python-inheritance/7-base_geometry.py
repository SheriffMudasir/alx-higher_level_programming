#!/usr/bin/python3
"""This module implements a class BaseGeometry"""


class BaseGeometry:
    """This is an empty class representing basic geometry operations."""

    def area(self):
        """This function raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function validates the variable value"""
        if not isinstance(value, int):
            # Use 'name' parameter
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            # Use 'name' parameter
            raise ValueError(f"{name} must be greater than 0")