#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    all_keys = list(sorted((a_dictionary.keys())))
    for key in all_keys:
        print("{}: {}".format(key, a_dictionary[key]))
