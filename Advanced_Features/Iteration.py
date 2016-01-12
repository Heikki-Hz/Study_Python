#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#Iteration test

#dict
d = {'a':1, 'b':2, 'c':3}
L = ['A', 'B', 'C']
List = [(1, 1), (2,3), (3,9)]

for key in d:
    print(key)

print('\n')

for value in d.values():
    print(value)


print('\n')

for key, value in d.items():
    print('%s: %d'%(key, value))

print('\n')
for i, vlaue in enumerate(L):
    print(i, vlaue)

print('\n')
for x, y in List:
    print('(%d, %d)'%(x, y))


