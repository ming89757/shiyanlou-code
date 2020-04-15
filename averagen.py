#!/usr/bin/env python3
number = int(input('Enter number :'))
s = 0
a = 0
while a < number:
    a += 1
    b = int(input("n"))
    s += b
print("sum is {},num is {}".format(s,a))
print('avg is {}'.format(s/a))
