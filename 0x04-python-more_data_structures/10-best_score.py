#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    all_keys = list(a_dictionary.keys())
    max_index = all_keys[0]
    for key in all_keys:
       max_index  = key if a_dictionary[key] > a_dictionary[max_index] else max_index
    return max_index
