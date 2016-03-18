#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
    def printscore(self):
        print('%s: %s' % (self.name, self.score))
    
    def entername(self):
        self.name = input('Please enter your name:')

    def enterscore(self):
        self.score = int(input('Please input your score:'))
    
    def get_grade(self):
        if self.score > 90:
            print('A')
            return 0
        if self.score >= 80:
            print('B')
            return 0
        if self.score >= 60:
            print('C')
            return 0
        else:
            print('E')
            return 0
#test

# name  = 'Heikki'
# score = 100
# test = Student(name,score)
# test.entername()
# test.enterscore()
# test.printscore()
# test.get_grade()

tmp = Student('Tom', 10)
#tmp.printscore()
print(tmp.name)

