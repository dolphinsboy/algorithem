#!/usr/bin/env python

def get_sum_square_smallthan_n(n):
    return sum([k*k for k in range(1,n)])

print get_sum_square_smallthan_n(10)
