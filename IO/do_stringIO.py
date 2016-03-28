#!/usr/bin/env python3
# -*- coding: utf-8 coding

from io import StringIO

f = StringIO()
f.write('Hello')
f.write(' ')
f.write('World')

print(f.getvalue())
print('---------------------')

Str = StringIO('Hello\nHi\nGood night!')

while True:
    s = Str.readline()
    if s == '':
        break
    print(s.strip())
