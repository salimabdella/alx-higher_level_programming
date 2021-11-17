#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 123:
            c = chr(ord(c) - (97 - 65))
        print("{:s}".format(c), end='')
    print("")
