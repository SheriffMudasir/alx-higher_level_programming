#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = (map(lambda x: replace if x == search else x, my_list))
    list_new_list = list(new_list)
    return (list_new_list)
