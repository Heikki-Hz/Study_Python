#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#str2int()
from functools import reduce

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,  
        '7': 7, '8': 8, '9': 9}
s = input('Please input str:')
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return d[s]
    return reduce(fn, map(char2num, s))
print('The s‘s type is', type(s))
print(str2int(s))
print('After ccomversion ', type(str2int(s)))


