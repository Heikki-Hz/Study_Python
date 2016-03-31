#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print(os.name)
print(os.uname())
# print(os.environ)
print('------------')
# print(os.environ.get('PATH'))
print(os.path.abspath('.'))
print(os.path.join(os.path.abspath('.'), 'testdir'))
dir = os.path.join(os.path.abspath('.'), 'testdir')

# print(os.mkdir(dir))
# os.rmdir(dir)

# os.rename('test.txt', 'test.py')
os.remove('test.py')
