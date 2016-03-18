#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print__score(self):
        print('%s: %s' % (self.__name, self.__score))
    
    def enter__name(self):
        self.__name = input('Please enter your name:')

    def enter__score(self):
        self.__score = int(input('Please input your score:'))
    
    def get_grade(self):
        if self.__score > 90:
            print('A')
            return 0
        if self.__score >= 80:
            print('B')
            return 0
        if self.__score >= 60:
            print('C')
            return 0
        else:
            print('E')
            return 0
#test
tmp = Student('Tom', 10)
#tmp.print__score()
print(tmp.__name)

