#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Heikki Huang'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello Wrold!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        _private_1(name)
    else:
        _private_2(name)

if __name__ == '__main__':
    test()
