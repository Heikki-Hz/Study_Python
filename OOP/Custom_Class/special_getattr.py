#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self):
        self.name = 'Heikki'

    def __str__(self):
        return 'Student object (name : %s)' % self.name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        
        if attr == 'age':
            return 25

        return AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

class China(object):
    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        return China('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr = __str__

#test
s = Student()
print('\'Student\'score is \'%s\'' % s.score)
print('\'Student\'age is \'%s\'' % s.age)

# print(China().status.user.timeline.list)
print(China().status.user)
