#!/usr/bin/python3
"""This module contain a base class"""
class Base:
    """This is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects