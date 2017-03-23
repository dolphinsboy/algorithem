#!/usr/bin/env python

def get_sum_square_odd_smallthan_n(n):
    return sum([k*k for k in range(1,n) if k % 2 == 1])

print get_sum_square_odd_smallthan_n(10)
