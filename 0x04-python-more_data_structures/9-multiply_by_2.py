#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    all_keys = list(a_dictionary.keys())
    new_dictionary = {}
    for key in all_keys:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary
