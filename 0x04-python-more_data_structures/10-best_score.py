#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    best_value = 0
    for key in a_dictionary:
        if key > best_value:
            best_value = key
    return best_value