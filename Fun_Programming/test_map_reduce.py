#!/usr/bin/evn python3
# -*- coding:utf-8 -*-

from functools import reduce

#str2float
d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,  
                '7': 7, '8': 8, '9': 9}

def str2float(s):
    def f(x, y):
        return x*10 + y
    def char2num(s):
        # return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
                # '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
        return d[s]
    s1,s2 = s.split('.')
    return reduce(f, map(char2num, s1)) + (reduce(f,map(char2num, s2))/pow(10,len(s2)))

print('str2float(\'123.456\') =', str2float('123.456'))
