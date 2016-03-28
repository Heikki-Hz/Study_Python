#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

def foo(s):
    return 10 / s

def bar(s):
    return foo(s) * 2

def main():
    try:
        ret = bar(s)
        print('ret = %d' % ret)
    except Exception as e:
        logging.exception(e)
    finally:
        print('End')

s = 0
main()
