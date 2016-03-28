#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print(os.name)
print(os.uname())
print(os.environ)
print('------------')
print(os.environ.get('PATH'))
print(os.path.abspath('.'))
