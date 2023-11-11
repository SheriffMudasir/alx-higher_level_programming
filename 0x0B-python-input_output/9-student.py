#!/usr/bin/python3
"""This contain function  Write jist for class"""
from 8-class_to_json import class_to_json

class Student:
    """A class student"""
    def __init__(self, first_name, last_name, age):
        """This function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A class"""
        return class_to_json(self)
