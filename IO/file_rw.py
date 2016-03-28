#!/usr/bin/env python3
# -*- coding: utf-8 -*-
f = 0 
try:
    f = open('/home/heikki/test/test.txt', 'r')
    # f = open('/home/heikki/test/test1.txt', 'r')
    print(f.read())
finally:
    f.close

with open('/home/heikki/test/Makefile', 'r') as f:
    for line in f.readlines():
        print(line.strip())
