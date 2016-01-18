#!/usr/vin/env python3
#coding:utf-8 

def is_odd(n):
    return n % 2 ==1
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(is_odd, List)))

def not_empty(s):
    return s and s.strip()
s = ['A', None, 'B', '']
print(list(filter(not_empty, s)))


#用filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

# for n in primes():
    # if n < 1000:
        # print(n)
    # else:
        # break

#回数
def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))





