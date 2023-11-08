#!/usr/bin/python3
""""This module contain one function that append a text to a file"""
def append_write(filename="", text=""):
    """This function appends a string at the end of a text file and returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as f:
        count = f.write(text)
    return count

