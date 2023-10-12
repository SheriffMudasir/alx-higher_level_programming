#!/usr/bin/python3
def number_keys(a_dictionary):
    list_of_keys = list(a_dictionary.keys())
    number_keys = 0


    for i in list_of_keys:
        number_keys += 1


    return (number_keys)