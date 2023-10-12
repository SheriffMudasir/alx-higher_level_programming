#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_item = list(a_dictionary.keys())

    for dict in keys_item:
        if value == a_dictionary.get(dict):
            del a_dictionary[dict]

    return (a_dictionary)
