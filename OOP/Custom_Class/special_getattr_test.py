#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class China(object):
    def __init__(self, path = ''):
        self._path = path

    def users(self, name):
        self._name = name
        return China('%s/%s' % (self._path, self._name))

    def __getattr__(self, path):
        if path == 'users':
            print('111')
            return China('%s/%s' % (self._path, self._name))
        return China('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr = __str__

#test
print(China().status.user.timeline.list)
print(China().status.users('Heiki').timeline.list)
