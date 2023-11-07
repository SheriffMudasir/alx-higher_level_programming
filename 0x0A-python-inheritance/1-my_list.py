#!/usr/bin/python3
"""This module prints a list in sorted order"""

class MyList(list):
    """This is the MyList class"""

    def print_sorted(self):
        """This function prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)