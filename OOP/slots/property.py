#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class Student(object):
#property :把一个getter方法变成属性
    @property
    def score(self):
        return self.__score

#负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be intger!')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0~100!')
        self.__score = value

s = Student()
s.score = 100
print('s.score = ', s.score)
s.score = 1000
print('s.score = ', s.score)
