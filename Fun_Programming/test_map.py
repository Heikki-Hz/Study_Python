#!/usr/bin/env python3
#-*- coding:utf-8 -*-


#纠正不规范的英文名字
def normalize(name):
    return name.title()
def normalize1(name):
    return name[0].upper() + name[1:].lower()
#name = ['HeiKKi', 'TOM', 'barT']
name = []
name.append(input('Please input your name:'))
name2 = list(map(normalize, name))
name3 = list(map(normalize1, name))
print('Your name is %s ?' % name2)
print('Your name is %s ?' % name3)
