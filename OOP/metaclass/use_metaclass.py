#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class Mylist(list, metaclass = ListMetaclass):
    pass

L = Mylist()
L.add(11)
print(L[0])
