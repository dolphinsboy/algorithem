#!/usr/bin/env python

import random

def choice(data):
    count = len(data)
    idx = random.randrange(0,count)

    return data[idx]

data = range(0, 10)
print choice(data)

