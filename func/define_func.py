#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#����һ������
def my_abs(x):
    if x >= 0:
        return x
    else:
        return(-x)

n = 10
m = -19

print(my_abs(n))
print(my_abs(m))

#�պ���
def nop():
    pass

#�����Ĳ���
def power(argv1, argv2 = 2):
    s = 1
    tmp = argv2
    while(argv2 > 0):
        argv2 = argv2 - 1
        s = s * argv1 
    print('%d-th power %d is %d' % (tmp, argv1,  s))
    return s

power(2, 4)
power(5)
power(3, 3)

