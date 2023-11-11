#!/usr/bin/python3
"""This module contain a function which add all argument to a list"""
from 5-save_to_json_file import save_to_json_file
def add_args(*args):
    """This function add all arguments to a python list"""
    filename = 'file.txt'
    json_file = 'add_item.json'
    python_list = []
    for i in args.items():
        python_list.append[i]
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(python_list)
    save_to_json_file(json_file, filename)



