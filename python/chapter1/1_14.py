#!/usr/bin/env python

def get_product_odd(data):
    odd_list = []
    count = len(data)
    i = 0

    while i < count:
        j = i + 1
        while j < count - 1:
            if data[i] * data[j] % 2 and data[i] != data[j]:
                odd_list.append((data[i], data[j]))
            j+=1
        i+=1
    return odd_list

data = range(1,10)
print get_product_odd(data)


