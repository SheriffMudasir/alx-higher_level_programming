#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict = a_dictionary.copy()
    list_keys = list(dict.keys())

    new_dict = map(lambda X: X*2, list_keys)

    return (new_dict)