#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import reduce

#higher-order func
f = abs
print('abs(-10) = ', abs(-10))
print('f(-10) = ', f(-10))
print('Use th abs itself', abs)
print('Use the f itself',f)
print('\n')

#Fun name is a variable
abs = 10
print(abs)
#print(abs(-19))
print('\n')

#Incoming function
x = int(input('Please input a integer:'))
y = int(input('Please input a integer:'))
def add(x, y, f):
    return f(x) + f(y)
print('After add is', add(x, y, f))
print('\n')

#map() function test
print('map() function test')
def my_square(x):
    return x * x
List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
List2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = map(my_square, List)
print('After computing the new list is ', list(result))
print('After conversion for the str ', list(map(str, List)))

#reduce() function test
def my_add(x, y):
    return x + y - 1
print(list(map(my_add, List, List2)))
print('After computing the result is ', reduce(my_add, List))



