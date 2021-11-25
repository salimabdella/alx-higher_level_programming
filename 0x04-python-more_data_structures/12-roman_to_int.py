#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False: 
        return 0
    roman_letters = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    maxchar = 'I'
    total = 0
    for i in roman_string[::-1]:
        if roman_letters[i] >= roman_letters[maxchar]:
            maxchar = i
            total += roman_letters[i]
        else:
            total -= roman_letters[i]
    return total
