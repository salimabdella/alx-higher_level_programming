#!/usr/bin/python3

for c in range(122, 97 - 1, -1):
    print("{:c}".format((c - (97 - 65)) if c % 2 else c), end='')
