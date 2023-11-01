#!/usr/bin/python3
"""This file contains one function print name"""
def say_my_name(first_name, last_name=""):
        """
        This function unction that prints My name is <first name> <last name>.

        Args:
                a (str): <first name>
                b (str): <last name>.

        """
        if not isinstance(first_name, (str)):
                raise TypeError("first_name must be a string")
        if not isinstance(last_name, (str)):
                raise TypeError("last_name must be a string")
        print(F"My name is {first_name} {last_name}")
say_my_name("John", "Smith")