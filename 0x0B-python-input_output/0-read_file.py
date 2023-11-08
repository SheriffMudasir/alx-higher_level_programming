#!/usr/bin/python3
""""This module contain one function that read a text file"""
def read_file(filename=""):
    """This function read a text file and print to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
