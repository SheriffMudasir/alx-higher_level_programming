#!/usr/bin/python3
""""This module contain one function that write a text to a file"""
def write_file(filename="", text=""):
    """This function write a text to a file and return the count"""
    count = 0
    with open(filename, 'w', encoding='utf-8') as file:
        count = file.write(text)
    return count
