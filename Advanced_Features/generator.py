#!/usr/bin/env python3
#-*- coding:utf-8 -*-

g = (x * x for x in range(10))
print(g)
for x in g:
    print(x)

#Feibolaqi series
def fib(max):
    n, a, b = 0, 0, 1
    while (n < max):
        print(b)
        (a, b) = (b, a + b)
        n = n + 1
    return 'done'

fib(6)
print('\n')

def fib(max):
    n, a, b = 0, 0, 1
    while (n < max):
        yield(b)
        (a, b) = (b, a + b)
        n = n + 1
    return 'done'

n = int(input("Please input a number:"))
for x in fib(n):
    print(x)

