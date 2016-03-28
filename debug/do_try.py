#!/usr/bin/env python3
# -*- coding: utf-8 -*-

i = int('2')

try:
    print('try ....')
    r = 10/i
    print('result:', r)
except ValueError as e:
    print('except:', e)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('No error!')
finally:
    print('finally ..')

print('END')
print('-----------------------')


def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        ret = bar(s)
        print('ret = %d' % ret)
    except Exception as e:
        print('Error:', e)
    finally:
        print('End')
s = 0
main()
