#!/usr/bin/env python

def jude_distinct(data):
    hash_dict = {}
    flag = True

    for i in data:
        if i in hash_dict:
            flag = False
            break
        else:
            hash_dict[i] = 0
    return flag

print jude_distinct([1,2,3,4])
print jude_distinct([1,2,3,4,4])

