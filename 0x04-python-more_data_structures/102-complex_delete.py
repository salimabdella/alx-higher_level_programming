#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    all_keys = list(a_dictionary.keys())
    for key in all_keys:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
