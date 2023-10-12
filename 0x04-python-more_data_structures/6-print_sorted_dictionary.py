#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_list = list(a_dictionary.keys())
    dict_list.sort()
    
    for i in dict_list:
        print("{}: {}".format(i, a_dictionary.get(i)))
