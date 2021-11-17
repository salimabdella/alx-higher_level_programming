#!/usr/bin/python3
import random


random_number = random.randint(-10000, 10000)
if random_number < 0:
    remainder = random_number % -10
else:
    remainder = random_number % 10
print('Last digit of', random_number, 'is', remainder, end=' ')
if remainder > 5:
    print('and is greater than 5')
elif remainder == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
