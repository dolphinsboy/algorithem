#!/usr/bin/env python

def reverse(data):
    i = 0
    j = len(data)-1

    while i < j:
        data[i], data[j] = data[j], data[i]
        i += 1
        j -= 1

data = range(0, 10)
reverse(data)
print data
