#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from functools import reduce
def fu(x ,y):
    return x * y
def prod(L):
    return reduce(fu, L)

L  = [1, 2, 3, 4]
L1 = [1, 3, 5, 7]

print(prod(L))
print(prod(L1))




