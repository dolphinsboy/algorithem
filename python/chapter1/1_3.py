#!/usr/bin/env python

import sys

def get_max_min(arr):
    max_val = -sys.maxint-1
    min_val = sys.maxint

    for i in arr:
        if i < min_val:
            min_val = i

        if i > max_val:
            max_val = i
    return (min_val, max_val)

print get_max_min([-1])
print get_max_min([-1,1,10,20,30])
